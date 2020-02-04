#!/usr/bin/python3
'''
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
'''


import csv
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

    url_todo = ("https://jsonplaceholder.typicode.com/todos?userID={}".
                format(employee_ID))
    response_todo = requests.get(url_todo)
    todo_dict = response_todo.json()

    with open("{}.csv".format(employee_ID), 'a+') as csvf:
        f = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo_dict:
            f.writerow([employee_ID, user_dict.get('username'),
                        task.get('completed'), task.get('title')])
