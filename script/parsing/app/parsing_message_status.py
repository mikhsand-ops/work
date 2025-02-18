import psycopg2
import json
import traceback
from log_factory import LoggerFactory
from sqlalchemy.engine import Connection
from sqlalchemy import text
from db_factory import DatabaseFactory
import os
import time

APP_VERSION = os.environ.get("APP_VERSION", "0.0.1-alpha1a")
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

# def run(conn: Connection):

logger.debug(f"opening file: ")


with open('message_status_january.csv','r') as f:
    lines = f.readlines()
    a = 0
    count_company_id = 0

    # logger.error(f"general error, {traceback.format_exc()}")
    logger.debug(f"splitting strings: ")

    for line in lines:
        a+=1
        if a == 1: continue
        data_split = line.split(',')
        # data = data_split[4]
        # print(data_split[2])
        # data_ril = json.loads(data.replace("\"\"","\"")[1:-2])

        total_len = data_split[0] + data_split[1] + data_split[2] + data_split[3]
        data_raw = line[len(total_len)+4:].strip()
        data_ril = json.loads(data_raw[1:-1].replace("\"\"","\""))
        wamid = data_split[2]

        # logger.debug(data_split)
        conversation_id = ''
        origin_type = ''
        phone_number_id = ''
        display_phone_number = ''
        status = ''
        tstamp = ''
        expiration_date = '0'
        category = ''
        billable = '0'
        pricing_model = ''
        data = '{}'

        value = data_ril['entry'][0]['changes'][0]['value']
        # logger.debug(value)
        if 'statuses' in value:
            statuses = value['statuses'][0]
            status = statuses['status']
            tstamp = statuses['timestamp']
            # conversation = statuses['conversation']
            if 'conversation' in statuses: # MESSAGE DELIVERED
                conversation_id = statuses['conversation']['id']
                origin_type = statuses['conversation']['origin']['type']
                if 'expiration_timestamp' in statuses['conversation']:
                    expiration_date = statuses['conversation']['expiration_timestamp']
                # print(expiration_date)
                    # expiration_date = str(expiration_date)     
            if 'pricing' in statuses:
                category = statuses['pricing']['category']
                billable = statuses['pricing']['billable']
                if billable == True: 
                    billable = '1' 
                else: 
                    billable = '0'
                pricing_model = statuses['pricing']['pricing_model']
        if 'messages' in value: # TYPE IMAGE
            tstamp = value['messages'][0]['timestamp']
        phone_number_id = value['metadata']['phone_number_id']
        display_phone_number = value['metadata']['display_phone_number']
        # print(value)
        
        if status == 'read' or status == 'deleted':
            logger.debug(f"status : " + status + " ...continuing")
            continue
        logger.debug("mencari company_id dengan phone_number " + str(display_phone_number))
        # print("mencari company_id dengan phone_number: " + str(display_phone_number))

        select_query = f"""SELECT company_id from whatsapp_phone_number 
                    where phone_number = '{display_phone_number}'"""
        # cur.execute(select_query)
        # company_id = conn.fetchone()[0]
        # count = 0
        try:
            cur.execute(select_query)
            company_id = cur.fetchone()[0]
            count_company_id +=1
            logger.debug(f"end getting id, count: {count_company_id}")
        except Exception:
            logger.error(traceback.format_exc())
            logger.error(select_query)
            

        if company_id is not None:

            logger.debug(f"dapat company_id dengan id : " + str(company_id))
            # print("dapat company_id dengan id: " + str(company_id))
            logger.debug(f"begin insert data with id : " + str(company_id))
            # print(id[0])
            insert_query = f"""INSERT INTO test (conversation_id,reference_id,session_type,phone_id,phone_number,st,
                            created_tstamp,expired_tstamp,category,billable,pricing_model,data,company_id) VALUES (
                            '{conversation_id}','{wamid}','{origin_type}','{phone_number_id}','{display_phone_number}',
                            '{status}',{tstamp},{expiration_date},'{category}',{billable},'{pricing_model}','{data}','{company_id}')
                            ON CONFLICT (conversation_id)
                            DO UPDATE SET
                            st = EXCLUDED.st
                            """      
            # print("mencoba menjalankan insert query:" + insert_query)
            # rowcount = 0              
            try:
                cur.execute(insert_query)
                # rowcount = res.rowcount
                conn.commit()
                logger.debug("success insert data ")
            except Exception:
                logger.error(f"error insert chat conversations {traceback.format_exc()}")
                time.sleep(1)
            logger.debug(f"end insert chat status, conversations: ")

            # print(insert_query)
        else:
            print ("tidak mendapatkan company_id")
            insert_query = f"""INSERT INTO test (conversation_id,reference_id,session_type,phone_id,phone_number,st,
                            created_tstamp,expired_tstamp,category,billable,pricing_model,data,company_id) VALUES (
                            '{conversation_id}','{wamid}','{origin_type}','{phone_number_id}','{display_phone_number}',
                            '{status}',{tstamp},{expiration_date},'{category}',{billable},'{pricing_model}','{data}','0')
                            ON CONFLICT (conversation_id)
                            DO UPDATE SET
                            st = EXCLUDED.st
                            """
            print("mencoba menjalankan insert query:" + insert_query)
            try:
                cur.execute(insert_query)
                conn.commit()
                # rowcount = res.rowcount
                logger.debug("success insert data ")
            except Exception:
                logger.error(f"error insert chat conversations {traceback.format_exc()}")
                time.sleep(1)
            logger.debug(f"end insert chat status, conversations: ")
        # print(insert_query)


# print("conversation_id: " + conversation_id)
        # print("origin_type: " + origin_type)
        # print("phone_number_id: " + phone_number_id)
        # print("display_phone_number: " + display_phone_number)
        # print("status: " + status)
        # print("tstamp: " + tstamp)
        # print("category: " + category)
        # print("billable: " + billable)
        # print("pricing_model: " + pricing_model)
        # print("expired_tstamp: " + expiration_tstamp)