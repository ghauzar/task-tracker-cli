import unittest
import json
import os
from task_manager import add_task, load_tasks, save_tasks, generate_unique_id

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_task_list.json"
        self.original_task_file = "task-list.json"

        if os.path.exists(self.original_task_file):
            os.rename(self.original_task_file, self.test_file)

        save_tasks({"tasks": []})

    def tearDown(self):
        if os.path.exists("task-list.json"):
            os.remove("task-list.json")
        if os.path.exists(self.test_file):
            os.rename(self.test_file, self.original_task_file)

    def test_add_task(self):
        task = add_task("Learn Python Unit Test")
        tasks = load_tasks()["tasks"]

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["description"], "Learn Python Unit Test")
        self.assertEqual(tasks[0]["status"], "todo")

    def test_generate_unique_id(self):
        tasks = [{"id": 1}, {"id": 2}, {"id": 3}]
        new_id = generate_unique_id(tasks)
        self.assertEqual(new_id, 4)  # ID baru harus 4

        tasks.append({"id": 4})
        new_id = generate_unique_id(tasks)
        self.assertEqual(new_id, 5)

if __name__ == "__main__":
    unittest.main()
