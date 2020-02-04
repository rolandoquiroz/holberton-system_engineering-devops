#!/usr/bin/python3
'''
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''


if __name__ == '__main__':
    '''
    This won't be run when imported """
    '''
    import requests
    from sys import argv

    employee_ID = argv[1]

    url_user = ("https://jsonplaceholder.typicode.com/users/{}".
                format(employee_ID))
    response_user = requests.get(url_user)
    user_dict = response_user.json()

    url_todo = ("https://jsonplaceholder.typicode.com/todos?userId={}".
                format(employee_ID))
    response_todo = requests.get(url_todo)
    todo_dict = response_todo.json()

    tasks_done = []

    for task in todo_dict:
        if task.get('completed'):
            tasks_done.append(task.get('title'))

    total_tasks = len(todo_dict)

    name = user_dict.get('name')

    print("Employee {} is done with tasks({}/{}):".
          format(name, len(tasks_done), total_tasks))

    for task in tasks_done:
        print("\t {}".format(task))