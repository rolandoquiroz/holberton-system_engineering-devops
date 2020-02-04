#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''


import json
import requests
import sys

if __name__ == "__main__":
    '''
    This won't be run when imported
    '''

    employee_ID = sys.argv[1]

    url_user = ("https://jsonplaceholder.typicode.com/users/{}".
                format(employee_ID))
    response_user = requests.get(url_user)
    user_dict = response_user.json()

    url_todo = ("https://jsonplaceholder.typicode.com/todos?userId={}".
                format(employee_ID))
    response_todo = requests.get(url_todo)
    todo_dict = response_todo.json()

    tasks_done = []
    my_dict = dict()

    for task in todo_dict:
        my_dict["task"] = task.get('title')
        my_dict["completed"] = task.get('completed')
        my_dict["username"] = user_dict.get('username')
        tasks_done.append(my_dict)
    json_file = dict()
    json_file[employee_ID] = tasks_done
    with open("{}.json".format(employee_ID), "a+") as jsf:
        json.dump(json_file, jsf)
