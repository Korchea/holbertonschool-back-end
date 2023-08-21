#!/usr/bin/python3
"""This script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    req = "https://jsonplaceholder.typicode.com/users/{}"
    req_all_task = "https://jsonplaceholder.typicode.com/todos"
    task_done = 0
    task_count = 0
    id = int(argv[1])
    req_users = requests.get(req.format(id)).json()
    req_all = requests.get(req_all_task).json()
    for all in req_all:
        if all['userId'] == id:
            task_count += 1
        if all['userId'] == id and all['completed'] is True:
            task_done += 1
    EMPLOYEE_NAME = req_users['name']
    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks({task_done}/{task_count}):")
    for all in req_all:
        if all['userId'] == id and all['completed'] is True:
            print(f"\t {all['title']}")
