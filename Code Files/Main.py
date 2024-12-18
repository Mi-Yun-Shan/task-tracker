from Task import Task

if __name__ == "__main__":
    task_manager = Task()

    Task.clear_tasks(task_manager)
    # Adding tasks
    task_manager.add_task(1, "Do laundry")
    task_manager.add_task(2, "Write report", status="in progress")
    task_manager.add_task(3, "Grocery shopping")
    Task.print_tasks(task_manager)
    Task.print_todo(task_manager)
    Task.print_in_progress(task_manager)