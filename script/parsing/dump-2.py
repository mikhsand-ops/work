import psycopg2
import datetime
import json
import csv
import time
import traceback
from log_factory import LoggerFactory
import os
import time

APP_VERSION = os.environ.get("APP_VERSION", "dumper-0.0.1-alpha1a")
DB_USER = os.environ.get('DB_USER', "postgres")
DB_PASS = os.environ.get('DB_PASS', "user")
DB_HOST = os.environ.get('DB_HOST', "localhost")
DB_PORT = os.environ.get('DB_PORT', "5432")
DB_NAME = os.environ.get('DB_NAME', "test")

lf = LoggerFactory(app_version=APP_VERSION)
logger = lf.get_logger("main")

conn = psycopg2.connect(
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME)
cur = conn.cursor()

now = datetime.datetime.now()
date = now.strftime('%Y%m%d')

current_time = time.time()
epoch_now = int(current_time)
from_epoch = 1704067201
label = []
write_result = []

query = f"""
    SELECT * FROM test WHERE created_tstamp BETWEEN {from_epoch} AND {epoch_now} limit 3
"""
try:
    cur.execute(query)
    conn.commit()
    logger.debug("running query... ")
except:
    logger.error("error querying " + {traceback.format_exc()})

try:
    logger.debug("fetching data... ")
    result=(cur.fetchall())
    columns = [desc[0] for desc in cur.description]
except:
    logger.error("error fetching data " + {traceback.format_exc()})

try:
    for row in result:
        if columns not in label:
            label.append(columns)

        write_result.append(dict(zip(columns, row)))
        cur.close()
        conn.close()
except:
    logger.error("error compiling data")

try:
    
# Write to CSV
    csv_file_path = f'dumpTest-{date}.csv'

    # Write header
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()

    # Write data rows
    with open(csv_file_path, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writerows(write_result)
except:
    logger.error("error writing csv")