import mysql.connector
from config import DB_HOST, DB_USERNAME, DB_PASSWORD, DB_NAME

def get_connection():
    try:
        conn = mysql.connector.connect(
            host = DB_HOST,  # do not put host as hostname
            user = DB_USERNAME,  #do not put user as usename
            password = DB_PASSWORD,
            database = DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"DB_ERROR {err}")
        return None
    

