#!/usr/bin/env python3

import sys
import argparse, json
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

# main parser
parser = argparse.ArgumentParser(description="Task Tracker CLI")

# Add subparser
subparsers = parser.add_subparsers(dest='command', help='Available Commands')

# Subcommand 'add new task'
add_parser = subparsers.add_parser('add', help='Add a new task')
add_parser.add_argument('task', metavar='task', type=str, help='The task description')

# Subcommand 'update'
update_parser = subparsers.add_parser('update', help='Update task description')
update_parser.add_argument('task_id', metavar='task_id', type=int, help='The ID of the task to update')
update_parser.add_argument('update_task', metavar='update_task', type=str, help='The update of the task')

# Subcommand 'delete'
delete_parser = subparsers.add_parser('delete', help='Delete an existing task')
delete_parser.add_argument('task_id', metavar='task_id', type=int, help='ID of the task to delete')

# Subcommand 'list'
list_parser = subparsers.add_parser('list', help='List all tasks')

# Listing task by status
list_subparsers = list_parser.add_subparsers(dest='list_command', help='Filter list with tasks status')
for status in ["todo", "in-progress", "done"]:
    list_subparsers.add_parser(status, help=f'List tasks with \"{status}\" status')

# Subcommand 'todo'
todo_parser = subparsers.add_parser('todo', help='Update tasks status to \'todo\'')
todo_parser.add_argument('task_id', metavar='task_id', type=int, help='The ID of the task to status update')

# Subcommand 'mark-in-progress'
mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help='Update tasks status to \'in-progress\'')
mark_in_progress_parser.add_argument('task_id', metavar='task_id', type=int, help='The ID of the task to status update')

# Subcommand 'mark-done'
done_parser = subparsers.add_parser('mark-done', help='Update tasks status to \'done\'')
done_parser.add_argument('task_id', metavar='task_id', type=int, help='The ID of the task to status update')

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

args = parser.parse_args()

if args.command == 'add':
    add_task(args.task)
elif args.command == 'delete':
    delete_task(args.task_id)
elif args.command == 'list':
    if args.list_command == 'todo':
        list_task('todo')
    elif args.list_command == 'in-progress':
        list_task('in-progress')
    elif args.list_command == 'done':
        list_task('done')
    else:
        list_task()
elif args.command == 'update':
    update_task(args.task_id,args.update_task)
elif args.command == 'todo':
    mark_task(args.task_id,"todo")
elif args.command == 'mark-in-progress':
    mark_task(args.task_id,"in-progress")
elif args.command == 'mark-done':
    mark_task(args.task_id,"done")

def main():
    print("Argument yang diterima:", sys.argv[1:])
if __name__ == "__main__":
    main()
