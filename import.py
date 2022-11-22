print ("helloworld")
import pandas as pd
empdata = pd.read_csv('~/task/uk-500.csv', index_col=False, delimiter = ',')
empdata.head()


import mysql.connector as mysql
from mysql.connector import Error
try:
    conn = mysql.connect(host='localhost', user='karlis',password='password')
#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE employee")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


import mysql.connector as mysql
from mysql.connector import Error
try:
    conn = mysql.connect(host='localhost', database='employee', user='karlis', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS employee_data;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE employee_data(first_name varchar(255),last_name varchar(255),company_name varchar(255),address varchar(255),city varchar(255),county varchar(255),postal varchar(255),phone1 varchar(255),phone2 varchar(255),email varchar(255),web varchar(255))")
        print("Table is created....")
        #loop through the data frame
        for i,row in empdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO employee.employee_data VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)
