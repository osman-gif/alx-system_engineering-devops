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
    emp_id = sys.argv[1]
    todo_url = f'https://jsonplaceholder.typicode.com/todos/'
    user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    user = requests.get(user_url)
    todos = requests.get(todo_url)
    t_tasks = 0
    all_tasks = []

    username = user.json().get('username')
    for index, todo in enumerate(todos.json()):

        if todo.get('userId') == int(emp_id):
            task = {}
            status = todo.get('completed')
            title = todo.get('title')
            task["task"] = title
            task["completed"] = status
            task["username"] = username
            # task_details = list([emp_id, username, str(status), title])
            # all_tasks.append(task)
            t_tasks = t_tasks + 1
            all_tasks.append(task)
    # with open(str(emp_id) + '.csv', 'x') as file:
    #     csv_writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    #     csv_writer.writerows(all_tasks)
    user = {emp_id: all_tasks}
    with open(str(emp_id)+".json", 'w') as file:
        json.dump(user, file)
