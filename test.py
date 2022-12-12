# Importing Libraries
import serial
import time
import sqlite3
arduino = serial.Serial(port='COM2', baudrate=9600, timeout=.1)
connection = sqlite3.connect("project.db")
cursor = connection.cursor()

def write_read():
    time.sleep(0.05)
    data = arduino.readline()
    return data

def get_data_from_db(card_id):
    """To get data based on card_id"""
    cursor.execute("SELECT members.full_name FROM members, lectures WHERE members.card_id='{}' AND members.card_id=lectures.card_id".format(card_id))
    return cursor.fetchone()[0]

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read().strip()
    print(value)
    value = value.decode('utf-8')
    print(get_data_from_db(value))





connection.close()
