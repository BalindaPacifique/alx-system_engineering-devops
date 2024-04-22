#!/usr/bin/python3
import sys
import requests
import csv

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

def export_to_csv(employee_id, todos):
    file_name = f"{employee_id}.csv"
    
    with open(file_name, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for todo in todos:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': todo['name'],
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    todos = get_employee_todo_progress(employee_id)
    
    export_to_csv(employee_id, todos)
