#!/usr/bin/python3
"""This Python script to export data in the CSV format."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    id = int(argv[1])
    txt = '"{}","{}","{}","{}"\n'
    req_users = requests.get(req.format(id)).json()
    req_all = requests.get(req_all_task).json()
    username_task = req_users['username']
    with open("{}.csv".format(id), "w") as file:
        for i in req_all:
            if i['userId'] == id:
                file.write(txt.format(id, username_task,
                                      i['completed'], i['title']))
