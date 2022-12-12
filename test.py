# Importing Libraries
import serial
import time
import sqlite3
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
connection = sqlite3.connect("project.db")
cursor = connection.cursor()

def write_read():
    time.sleep(0.05)
    data = arduino.readline()
    return data

def insert_to_db(card_id):
	try:
		cursor.execute("INSERT INTO members ('full_name', 'card_id', 'dr') VALUES ('DR Ahmed', '{}', '1')".format(card_id)
	except sqlite3.IntegrityError:
		return "Already used"
def get_data_from_db(card_id):
	"""To get data based on card_id"""
	cursor.execute("SELECT members.full_name FROM members, lectures WHERE members.card_id='{}' AND members.card_id=lectures.card_id".format(card_id))
	data = cursor.fetchall()
	if data:
		return data

while True:
	value = arduino.readline()
	time.sleep(1)
	if value:
		value = value.decode('utf-8')
		print(value)
		#insert_to_db(value.strip())
		print(get_data_from_db(value.strip()))





connection.close()
