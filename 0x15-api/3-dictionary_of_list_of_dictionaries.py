#!/usr/bin/python3
"""This is a Python script that, using this REST API
https://jsonplaceholder.typicode.com/todos/
it export data in the CSV format.
"""
import csv
import json
import requests
import sys

if __name__ == '__main__':
    todo_url = f'https://jsonplaceholder.typicode.com/todos/'
    user_url = f'https://jsonplaceholder.typicode.com/users/'

    users = requests.get(user_url)
    todos = requests.get(todo_url)
    t_tasks = 0
    all_tasks = []
    users_dict = {}
    usr = {}
    usrs = {}
    user_id = 0

    for user in users.json():
        userId = user.get("id")
        user_tasks = []
        username = user.get('username')
        for todo in todos.json():
            task = {}
            task['completed'] = todo.get('completed')
            task["task"] = todo.get('title')
            task["username"] = username
            # all_tasks.append(task)
            user_tasks.append(task)
        usr[userId] = user_tasks

    with open("todo_all_employees.json", 'w') as file:
        json.dump(usr, file)

    # username = users.json().get('username')
    # for index, todo in enumerate(todos.json()):

    #     if todo.get('userId') == int(emp_id):
    #         task = {}
    #         status = todo.get('completed')
    #         title = todo.get('title')
    #         task["task"] = title
    #         task["completed"] = status
    #         task["username"] = username

    #         t_tasks = t_tasks + 1
    #         all_tasks.append(task)

    # user = {emp_id: all_tasks}
    # with open(str(emp_id)+".json", 'w') as file:
    #     json.dump(user, file)
