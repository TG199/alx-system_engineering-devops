#!/usr/bin/python3
"""
Employee API
"""
import requests
import sys


def get_employee_progress(employee_id: int):
    base_url: str = "https://jsonplaceholder.typicode.com"
    employee_url: str = f"{base_url}/users/{employee_id}"
    todos_url: str = f"{base_url}/todos?userId={employee_id}"

    employee_reponse: str = requests.get(employee_url)
    if employee_reponse.status_code != 200:
        print("Failed to fetch employe info")
        return

    employee_data: str = employee_reponse.json()
    employee_name: str = employee_data['name']

    todos_response: str = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Failed to fetch employee's todos")
        return

    todos_data: str = todos_response.json()
    total_tasks: int = len(todos_data)
    done_task = [task for task in todos_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks
          ({len(done_task)}/{total_tasks}): ")
    for task in done_task:
        print(f"\t{task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: script EMLOYEE_ID')
        sys.exit(1)

    employee_id: int = int(sys.argv[1])
    get_employee_progress(employee_id)
