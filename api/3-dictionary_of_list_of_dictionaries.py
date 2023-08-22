#!/usr/bin/python3
"""This Python script to export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    req_all = requests.get(req_all_task).json()
    req_users = requests.get(req).json()
    to_json = {}
    for user in req_users:
        to_list = []
        to_dict = {}
        for i in req_all:
            if i['userId'] == user['id']:
                to_dict.update({"username": user['username']})
                to_dict.update({"task": i['title']})
                to_dict.update({"completed": i['completed']})
                to_list.append(to_dict)
        to_json.update({user['id']: to_list})
    with open("todo_all_employees.json", "w") as file:
        file.write(json.dumps(to_json))
