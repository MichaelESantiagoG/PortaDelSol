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

import sqlite3 as sql
import pandas as pd


def query1(query):
    conn = sql.connect("Database/portadelsol.db")
    # Execute the SQL query
    cursor = conn.execute(query)
    # Fetch the column names from the cursor description
    columns = [description[0] for description in cursor.description]
    # Fetch all rows from the cursor
    data = cursor.fetchall()
    # Convert the fetched data and column names to a DataFrame
    data_df = pd.DataFrame(data, columns=columns)
    # Return the DataFrame
    return data_df


def query2(query):
    conn = sql.connect("Database/portadelsol.db")
    conn.execute(query)
    conn.commit()
