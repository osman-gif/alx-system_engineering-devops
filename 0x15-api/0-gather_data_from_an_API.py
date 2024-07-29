#!/usr/bin/python3
import requests
import json
from sys import argv

emp_id = argv[1]
todo_url = f'https://jsonplaceholder.typicode.com/todos/'
user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

user = requests.get(user_url)
todos = requests.get(todo_url)
completed_tasks = 0
total_tasks = 0
tasks_title_list = []

emp_name = user.json().get('name')
for index, todo in enumerate(todos.json()):

    if todo.get('userId') == int(emp_id):
        total_tasks = total_tasks + 1

        if todo.get('completed'):
            tasks_title_list.append(todo.get('title'))
            completed_tasks = completed_tasks + 1

first_line = f"Employee {emp_name} is done with \
tasks({completed_tasks}/{total_tasks})"
print(first_line)
for task_title in tasks_title_list:
    print(f"     {task_title}")
