import sqlite3
# from faker import Faker
# fake = Faker()
# Initalize connection to DB
connection = sqlite3.connect("project.db")
cursor = connection.cursor()

# Random Name, ID generator for providiing fake data.
# for i in range(1,10):
#     query = """INSERT INTO members (full_name, card_id, dr) VALUES ("{}", '{}', "{}")""".format(fake.first_name(), fake.ean(length=8), i%2)
#     cursor.execute(query)
#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into table")

def get_data_from_db(card_id):
    """To get data based on card_id"""
    cursor.execute("SELECT members.full_name, lectures.LECTURE_NAME, members.card_id, lectures.start_at, lectures.end_at FROM members, lectures WHERE members.card_id='{}' AND members.card_id=lectures.card_id".format(card_id))
    return cursor.fetchall()

#get_data_from_db("A1")





connection.close()
