import argparse
from task_manager import add_task, list_task, update_task, delete_task, mark_task
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

