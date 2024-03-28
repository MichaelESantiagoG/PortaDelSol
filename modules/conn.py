# --------------------------------------------------------------------------------------------------
# """Database Connections"""
# """
#       class Connections:
#           |___def live_connect(database)
#           |___def connect()
#           |___def query1()
#           |___def query2()
# """
# --------------------------------------------------------------------------------------------------

import urllib
import pandas as pd
import pymssql
import streamlit as st


class Connections:
    @staticmethod
    def live_connect():
        SERVER = st.secrets.server
        DATABASE = st.secrets.database
        USERNAME = st.secrets.username
        PASSWORD = st.secrets.password
        params = {
            "server": SERVER,
            "database": DATABASE,
            "user": USERNAME,
            "password": PASSWORD,
            "autocommit": True,  # You can adjust this parameter as needed
        }
        try:
            conn = pymssql.connect(**params)
            return conn
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def query1(query):
        conn = Connections.live_connect()
        data = pd.read_sql_query(query, conn)
        return data

    def query2(query):
        conn = Connections.live_connect()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("Update or delete operation executed successfully.")
        except Exception as e:
            print(f"Error executing update or delete query: {e}")
        finally:
            conn.close()