#!/usr/bin/python3
"""This Python script to export data in the CSV format."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    user = ""
    id = int(argv[1])
    req_users = requests.get(req.format(id)).json()
    req_all = requests.get(req_all_task).json()
    filename = "{}.csv".format(id)
    with open(filename, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quoting=csv.QUOTE_MINIMAL)
        for all in req_all:
            if all['userId'] == id:
                work = all['completed']
                work_name = all['title']
                spamwriter.writerow([id, req_users['name'], work, work_name])
