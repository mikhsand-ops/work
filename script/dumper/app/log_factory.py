"""
LoggerFactory - A utility class for creating and configuring loggers
in Python applications.

Author: @dexterdmonkey
Created: September 7, 2023
License: MIT License
Version: 0.0.1

This module provides the LoggerFactory class,
which allows you to create and configure loggers with specific formatting
and handlers for both console (stdout) and file logging.
"""


from typing import Optional
from logging.handlers import TimedRotatingFileHandler

import logging


class LoggerFactory:
    """
    A utility class for creating and configuring loggers in Python applications.

    Args:
        app_version (str): The version of the application.
        log_file_path (str, optional): The path to the log file.
            If provided, logs will be written to this file.
    """

    def __init__(self, app_version: str, log_file_path: Optional[str] = None) -> None:
        self.log_file_path = log_file_path
        self.log_formatter = logging.Formatter(
            f"%(asctime)s - %(levelname)s - %(name)s - {app_version} - [%(process)d] - %(message)s"
        )

    def create_console_handler(self) -> logging.StreamHandler:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(self.log_formatter)
        return console_handler

    def create_file_handler(self, log_file_path: str) -> TimedRotatingFileHandler:
        file_handler = TimedRotatingFileHandler(log_file_path, "midnight", 1)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(self.log_formatter)
        return file_handler

    def get_logger(self, logger_name: str) -> logging.Logger:
        """
        Get a configured logger instance with the specified name.

        Args:
            logger_name (str): The name of the logger.

        Returns:
            logging.Logger: The configured logger instance.
        """

        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        ch = self.create_console_handler()
        logger.addHandler(ch)

        if self.log_file_path:
            fh = self.create_file_handler(self.log_file_path)
            logger.addHandler(fh)

        return logger

