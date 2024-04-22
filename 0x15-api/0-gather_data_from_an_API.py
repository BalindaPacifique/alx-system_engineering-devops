#!/usr/bin/python3
import sys
import requests

def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        todos = response.json()
        
        # Process the todos data to get the required information
        # Calculate number of done tasks and total tasks
        
        # Print the employee TODO list progress
        print(f"Employee {todos[0]['name']} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
