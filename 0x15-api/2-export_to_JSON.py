#!/usr/bin/python3
import sys
import requests
import json

def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todos = response.json()
        
        return todos
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_json(employee_id, todos):
    file_name = f"{employee_id}.json"
    
    data = {employee_id: []}
    
    for todo in todos:
        data[employee_id].append({
            'task': todo['title'],
            'completed': todo['completed'],
            'username': todo['name']
        })
    
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    todos = get_employee_todo_progress(employee_id)
    
    export_to_json(employee_id, todos)
