#!/usr/bin/python3
"""This Python script to export data in the CSV format."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    id = int(argv[1])
    req_users = requests.get(req.format(id)).json()
    req_all = requests.get(req_all_task).json()
    to_list = []
    to_dict = {}
    for i in req_all:
        if i['userId'] == id:
            to_dict.update({"task": i['title']})
            to_dict.update({"completed": i['completed']})
            to_dict.update({"username": req_users['username']})
            to_list.append(to_dict)
    to_json = {}
    to_json.update({id: to_list})
    with open("{}.json".format(id), "w") as file:
        file.write(json.dumps(to_json))
