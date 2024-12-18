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

    # CRUD methods

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

    def clear_tasks(self): # Overwrite the current file and start anew
        with open(self.file_name, "w") as tasks_file:
            tasks = []
            json.dump(tasks, tasks_file) # Write empty list to file

    def update_task(self):

        # Menu

        print("Incomplete Tasks: \n")
        Task.print_todo(self)
        Task.print_in_progress(self)

        # User input
        task_to_update = input("Which file would you like to update? >> ")
        new_status = input("What status would you like to update the task to? >> ")

        # Locate and update file
        with open(self.file_name, "r") as tasks_file:
            tasks = json.load(tasks_file)

            # Error handling
            try:
                tasks[int(task_to_update + 1)]["status"] = new_status # +1 to be user-friendly
            except KeyError:
                print("No such task")

            tasks[int(task_to_update + 1)]["updated_at"] = datetime.datetime.now().isoformat() # Update time to reflect update of record

            # Update description
            description_update_choice = input("Would you like to alter the description too? (Y/N) >>  ")
            if description_update_choice.lower() == "y":
                new_description = input("New description >> ")
                tasks[int(task_to_update + 1)]["description"] = new_description

            elif description_update_choice.lower() == "n":
                print("Description unchanged")
            else:
                print("Invalid input")


        # Write back to file
        with open(self.file_name, "w") as tasks_file:
            json.dump(tasks, tasks_file, indent=4)

    # Printing methods

    def print_tasks(self):
        with open(self.file_name, "r") as tasks_file:
            tasks = json.load(tasks_file)
            for task in tasks:
                print(f"{task['id']}: {task['description']}")

        print("\n")

    def print_todo(self):
        print("Tasks yet to be started: \n")
        with open(self.file_name, "r") as tasks_file:
            tasks = json.load(tasks_file)
            for task in tasks:
                if task['status'] == 'todo':
                    print(f"{task['id']}: {task['description']}")
        print("\n")

    def print_in_progress(self):
        print("Tasks in progress: \n")
        with open(self.file_name, "r") as tasks_file:
            tasks = json.load(tasks_file)
            for task in tasks:
                if task['status'] == 'in progress':
                    print(f"{task['id']}: {task['description']}")

        print("\n")

    def print_complete(self):
        print("Tasks completed: \n")
        with open(self.file_name, "r") as tasks_file:
            tasks = json.load(tasks_file)
            for task in tasks:
                if task['status'] == 'done':
                    print(f"{task['id']}: {task['description']}")

        print("\n")