# Task class
import datetime
import json
import os


class Task:
    def __init__(self, file_name = "Tasks.json"):
        self.file_name = file_name

        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as tasks_file:
                json.dump([], tasks_file)  # Initialize with an empty list

    def add_task(self, task_id, description, status="todo", created_at=None, updated_at=None):
        # Set default values for created_at and updated_at
        if created_at is None:
            created_at = datetime.datetime.now().isoformat()
        if updated_at is None:
            updated_at = datetime.datetime.now().isoformat()

        # Defining the JSON to be added
        task = {
            "id": task_id,
            "description": description,
            "status": status,
            "created_at": created_at,
            "updated_at": updated_at
        }

        # Load existing tasks
        try:
            with open(self.file_name, "r") as tasks_file:
                tasks = json.load(tasks_file)
        except (json.JSONDecodeError, FileNotFoundError):
            tasks = []  # If the file is empty or invalid, start with an empty list

        # Append the new task
        tasks.append(task)

        # Write the updated list of tasks back to the JSON file
        with open(self.file_name, "w") as tasks_file:
            json.dump(tasks, tasks_file, indent=4)  # Write as a pretty-printed JSON array




