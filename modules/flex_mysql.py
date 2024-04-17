import mysql.connector
import pandas as pd


def connect():
    cnx = mysql.connector.connect(
        user="SICI",
        password="CapyBara4097",
        host="testsici.mysql.database.azure.com",
        database="PortaDelSol",
    )
    cursor = cnx.cursor()
    return cnx, cursor


def query1(query):
    cxn, cursor = connect()
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    print(columns)
    data = cursor.fetchall()
    df = pd.DataFrame(data=data, columns=columns)
    return df


def query2(query):
    cxn, cursor = connect()
    cursor.execute(query)
    cxn.commit()
