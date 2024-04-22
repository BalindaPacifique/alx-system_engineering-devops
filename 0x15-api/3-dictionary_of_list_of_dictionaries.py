#!/usr/bin/python3
import json
import requests

def fetch_employee_data():
    # Make an HTTP request to fetch the employee data from the API
    response = requests.get('API_ENDPOINT_URL')
    data = response.json()
    return data

def organize_data(data):
    # Organize the data into the desired format
    organized_data = {}
    for item in data:
        user_id = item['userId']
        task = {
            'username': item['username'],
            'task': item['title'],
            'completed': item['completed']
        }
        if user_id in organized_data:
            organized_data[user_id].append(task)
        else:
            organized_data[user_id] = [task]
    return organized_data

def export_to_json(organized_data):
    # Export the organized data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(organized_data, json_file)

if __name__ == "__main__":
    # Fetch employee data from the API
    employee_data = fetch_employee_data()

    # Organize the data
    organized_data = organize_data(employee_data)

    # Export data to JSON
    export_to_json(organized_data)

