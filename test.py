import mysql.connector
from mysql.connector import Error
from faker import Faker
fake = Faker()

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='students_test_db',
                                         user='root')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        for i in range(1,10):
            query = """INSERT INTO students_docs_test_table	(card_id, id, name, role) VALUES ("1q2w3e4r5t", {}, "{}", 'student')""".format(i, fake.first_name())
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
