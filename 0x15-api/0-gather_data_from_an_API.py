#!/usr/bin/python3
"""This is a Python script that, using this REST API
https://jsonplaceholder.typicode.com/todos/
, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import json
import requests
import sys

if __name__ == '__main__':
    emp_id = sys.argv[1]
    todo_url = f'https://jsonplaceholder.typicode.com/todos/'
    user_url = f'https://jsonplaceholder.typicode.com/users/{emp_id}'

    user = requests.get(user_url)
    todos = requests.get(todo_url)
    c_tasks = 0
    t_tasks = 0
    tasks_title_list = []

    e_name = user.json().get('name')
    for index, todo in enumerate(todos.json()):

        if todo.get('userId') == int(emp_id):
            t_tasks = t_tasks + 1

            if todo.get('completed'):
                tasks_title_list.append(todo.get('title'))
                c_tasks = c_tasks + 1

    first_line = f"Employee {e_name} is done with tasks({c_tasks}/{t_tasks}):"
    print(first_line)
    for task_title in tasks_title_list:
        print(f"\t {task_title}")
