import requests

def check(val):
    response = requests.get("http://localhost/backend/check.php?id={}".format(val)).text
    print(response)

def add(val):
    response = requests.get("http://localhost/backend/add.php?id={}&role=1".format(val)).text
    print(response)

