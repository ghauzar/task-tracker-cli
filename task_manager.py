import json
from datetime import datetime
from pathlib import Path

# File path configuration
TASK_FILE = "task-list.json"

def load_tasks():
    if not Path(TASK_FILE).exists():
        save_tasks({"tasks" :[]})
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(data):
    with open(TASK_FILE, "w") as file:
        json.dump(data,file,indent=4)

def generate_unique_id(tasks):
    return max((task['id'] for task in tasks), default=0) + 1

# Load tasks data
data_tasks = load_tasks()

def add_task(description):
    new_task = {
        "id":generate_unique_id(data_tasks["tasks"]),
        "description": description,
        "status": "todo", # the default status of new task is "todo"
        "createAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    data_tasks["tasks"].append(new_task)
    save_tasks(data_tasks)
    print(f"Task '{description}' has been added.")
    print(f"Enter command 'python main.py list' to see all tasks.")

def list_task(status=''):
    filtered_tasks = data_tasks["tasks"] if not status else [task for task in data_tasks["tasks"] if task["status"] == status]
    title = "ALL TASKS" if not status else f'"{status.upper()}" TASKS' 

    print(f"{title}\nID \t Task Description")
    for task in filtered_tasks:
        print(f"{task['id']} \t {task['description']} ({task['status'].upper()})")

def update_task(task_id,task_update):
    for task in data_tasks["tasks"]:
        if task["id"] == task_id:
            task["description"] = task_update
            task["updatedAt"] = datetime.now().isoformat()
    save_tasks(data_tasks)
    print(f"Task with ID:'{task_id}' has been updated.")
    print(f"Enter command \'python main.py list' to see all tasks.")

def delete_task(task_id):
    confirm = input(f"Are you sure to delete the task(ID={task_id})? (y/n): ")
    # deletion confirmation
    if(confirm.lower() == 'y'):
        # delete task
        data_tasks["tasks"].pop(task_id-1)
        for task in data_tasks["tasks"]:
            if task["id"] > task_id:
                task["id"] -= 1
                task["updatedAt"] = datetime.now().isoformat()
        save_tasks(data_tasks)
        print(f"Task with ID:'{task_id}' has been deleted.")
        print(f"Enter command 'python main.py list' to see all tasks.")
    elif(confirm.lower() == 'n'):
        print(f"Task deletion aborted.")
    else:
        raise Exception(f"Invalid input. Please select between 'y' or 'n'")

def mark_task(task_id, status):
    for task in data_tasks["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
    save_tasks(data_tasks)
    print(f"Status of task with ID:'{task_id}' has been marked as \'{status}\'.")
    print(f"Enter command 'python main.py list' to see all tasks.")