"""
Database Connection Factory Module

Author: @dexterdmonkey
Created: September 7, 2023
License: MIT License
Version: 0.0.1

This module provides a factory class for managing database connections and engine initialization.
It allows you to configure the database connection either via a configuration file or individual
database parameters or both, with options for customizing the connection pool.

Classes:
    - DatabaseFactory: A factory class for managing database connections and engine initialization.

Usage:
    # Example usage of the DatabaseFactory class:
    factory = DatabaseFactory(config_file="database.ini")
    conn = factory.get_conn()
    # Use the 'conn' object for database operations.
"""

from typing import Optional, Dict, NamedTuple, Generator
from sqlalchemy import create_engine, text, exc
from sqlalchemy.engine.base import Engine, Connection
from sqlalchemy.pool import Pool, QueuePool, StaticPool
from sqlalchemy.orm import sessionmaker, Session

import traceback
import time
import logging


class DBStatus(NamedTuple):
    status: str
    version: Optional[str]
    error: Optional[str]


class DatabaseFactory:
    """
    A factory class for managing database connections and engine initialization.

    Args:
        db_engine (str, optional): The database engine, e.g., 'postgresql', 'mysql', etc.
        db_driver (str, optional): The database driver, e.g., 'psycopg2', 'mysql-connector', etc.
        db_user (str, optional): The database username.
        db_pass (str, optional): The database password.
        db_host (str, optional): The database host.
        db_port (str, optional): The database port.
        db_name (str, optional): The name of the database.
        config_file (str, optional): The path to the configuration file for database settings.
        logger (logging.Logger, optional): A custom logger for logging messages.
        pool_size (int, optional): The size of the database connection pool. Default is 1.
        max_overflow (int, optional): The maximum size to which the pool can overflow. Default is 15.
        connect_args (dict, optional): Additional connection arguments for the database engine.

    Raises:
        ValueError: If both config_file and individual database parameters are provided,
                    or if none of them are provided.
    """

    def __init__(
        self,
        db_url: Optional[str] = None,
        db_engine: Optional[str] = None,
        db_driver: Optional[str] = None,
        db_user: Optional[str] = None,
        db_pass: Optional[str] = None,
        db_host: Optional[str] = None,
        db_port: Optional[str] = None,
        db_name: Optional[str] = None,
        config_file: Optional[str] = None,
        logger: Optional[logging.Logger] = None,
        pool_size: int = 1,
        max_overflow: int = 15,
        connect_args: Optional[Dict] = None,
        poolclass = QueuePool,
    ) -> None:
        # Ensure that you can provide either a configuration file (config_file)
        # or individual database parameters (db_engine, db_driver, db_user, db_pass, db_host, db_port, db_name)
        # or both, but not none of them.

        if db_url is None and config_file is None and not any(
            (db_engine, db_driver, db_user, db_pass, db_host, db_port, db_name)
        ):
            raise ValueError(
                "You must provide either a configuration file (config_file) "
                "or individual database parameters or both, but not none of them."
            )
        
        self.db_url = db_url
        self.config_file = ""
        if config_file:
            self.config_file = config_file

        self.db_engine = db_engine
        self.db_driver = db_driver
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_port = db_port
        self.db_name = db_name
        
        self.poolclass = poolclass
        self.pool_size = pool_size
        self.max_overflow = max_overflow
        self.connect_args = connect_args

        if not connect_args:
            self.connect_args = dict()

        if logger is None:
            self.log = logging.getLogger(__name__)
            self.log.addHandler(logging.StreamHandler())
            self.log.setLevel(logging.DEBUG)
        else:
            self.log = logger
            
        self.engine: Optional[Engine] = None


    def _get_database_url(self) -> str:
        """
        Retrieve the database URL from the configuration file.

        Returns:
            str: The database URL constructed from the configuration.
        """
        
        if self.db_url is not None:
            return self.db_url
        
        try:
            with open(self.config_file, "r") as f:
                conf_string = f.read()
                return conf_string
        except Exception:
            self.log.info("Failed to read the config file. Using default values.")
            conf_string = ""

        return (
            f"{self.db_engine}+{self.db_driver}://{self.db_user}:{self.db_pass}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )

    def initialize_engine(self) -> Optional[Engine]:
        db_url = self._get_database_url()
        self.log.info(f"Creating a database engine: {db_url}")
        try:
            if self.poolclass == StaticPool:
                self.engine = create_engine(
                    db_url,
                    poolclass=self.poolclass,
                    connect_args=self.connect_args,
                    pool_pre_ping=True,
                )
            else:
                self.engine = create_engine(
                    db_url,
                    poolclass=self.poolclass,
                    pool_size=self.pool_size,
                    max_overflow=self.max_overflow,
                    connect_args=self.connect_args,
                    pool_pre_ping=True,
                )
        except Exception:
            self.log.error("Failed to create the database engine.")
            self.log.error(traceback.format_exc())
            return None
        
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

        return self.engine

    def get_conn(self, max_retries=5, retry_delay=2):
        """
        Retrieve a database connection, with the option to retry on failure.

        Args:
            max_retries (int, optional): The maximum number of retry attempts.  
                Default is 3.
            retry_delay (int, optional): The number of seconds to wait
                between retry attempts. Default is 2.

        Returns:
            SQLAlchemy database connection object,
                or None if all retry attempts fail.
        """

        conn = None

        if self.engine is None:
            self.initialize_engine()

        retry_count = 0
        while retry_count < max_retries:
            try:
                conn = self.engine.connect()
                break  # Connection successful, exit the loop
            except exc.SQLAlchemyError as e:
                self.log.error(f"Failed to create a database connection: {str(e)}")
                self.log.info(f"Retrying the connection in {retry_delay} seconds.")
                time.sleep(retry_delay)

                try:
                    self.dispose_engine()
                except Exception:
                    pass

                self.initialize_engine()
                retry_count += 1

        if conn is None:
            raise Exception("Failed to create a database connection")

        return conn

    
    def get_session(self, max_retries=5, retry_delay=2) -> Generator[Session, None, None]:
        """
        Retrieve a database connection, with the option to retry on failure.

        Args:
            max_retries (int, optional): The maximum number of retry attempts.
                Default is 3.
            retry_delay (int, optional): The number of seconds to wait
                between retry attempts. Default is 2.

        Returns:
            SQLAlchemy database connection object,
                or None if all retry attempts fail.
        """

        session = None

        if self.engine is None:
            self.initialize_engine()

        retry_count = 0
        while retry_count < max_retries:
            try:
                session = self.SessionLocal()
                break  # Connection successful, exit the loop
            except exc.SQLAlchemyError as e:
                self.log.error(f"Failed to create a database connection: {str(e)}")
                self.log.info(f"Retrying the connection in {retry_delay} seconds.")
                time.sleep(retry_delay)

                try:
                    self.dispose_engine()
                except Exception:
                    pass

                self.initialize_engine()
                retry_count += 1

        if session is None:
            raise Exception("Failed to create a database session")
        
        try:
            yield session
        finally:
            session.close()
    
    def get_db_status(self):
        status = "NOT OK"
        version = None
        error = None
        
        stmt = text("""
            SELECT VERSION()            
        """)
        
        try:
            with self.get_conn() as conn:
                res = conn.execute(stmt)
                row = res.fetchone()
                version, = row
                status = "OK"
        except Exception as err:
            self.log.error(traceback.format_exc())
            error = f"{err}"
            
        return DBStatus(
            status=status,
            version=version,
            error=error
        )

    def dispose_engine(self):
        """
        Dispose of the database engine if it exists.
        This releases any resources associated with the engine.
        """
        if self.engine is not None:
            self.engine.dispose()
