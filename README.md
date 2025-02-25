<h1>Task Tracker CLI Program</h1>
Simple Python CLI program to track daily tasks. All tasks were stored in a file with JSON format. Built for educational purposes. Simple unit tests are included.

<h3>Task Properties 👨‍💻</h3>
Each task has the following properties:
<ul>
  <li> <code>id</code> : A unique identifier for the task</li>
  <li> <code>description</code>: A short description of the task</li>
  <li> <code>status</code> : The status of the task (todo, in-progress, done)</li>
  <li> <code>createdAt</code>: The date and time when the task was created</li>
  <li> <code>updatedAt</code>: The date and time when the task was last updated</li>
</ul>

<h3>Features ✨</h3>
✅ Add new tasks <br>
✅ List all tasks <br>
✅ List tasks by status <br>
✅ Update tasks <br>
✅ Mark task's status (in-progress | done) <br>
✅ Delete tasks <br>

<h3>How to use 💻</h3>

Show Help Menu:
```
python main.py -h
```

Add new tasks (Default new task status is "todo"):
```
python main.py add "Your new task"
```

List all tasks:
```
python main.py list
```
List tasks by status:
```
python main.py list [todo | in-progress | done]
```

Update tasks:
```
python main.py update [task_id] "Your updated task"
```

Mark task's status 'in-progress':
```
python main.py mark-in-progress [task_id]
```

Mark task's status 'done':
```
python main.py mark-done [task_id]
```

Delete task:
```
python main.py delete [task_id]
```

Project URL ==> https://github.com/ghauzar/task-tracker-cli
