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

    e_name = user.json().get('name')
    for index, todo in enumerate(todos.json()):

        if todo.get('userId') == int(emp_id):
            status = todo.get('completed')
            title = todo.get('title')
            task_details = f'"{emp_id}","{e_name}","{status}","{title}"'

            all_tasks.append(task_details)
            t_tasks = t_tasks + 1

    with open('USER_ID.csv', 'x', newline='\n') as file:
        csv_writer = csv.writer(file, quotechar=' ')
        for task in all_tasks:
            csv_writer.writerow([task])