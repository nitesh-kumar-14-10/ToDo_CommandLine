import sqlite3

# Create a SQLite database and table for storing tasks
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    task TEXT,
    priority TEXT,
    due_date TEXT,
    completed INTEGER
)
''')
conn.commit()

def add_task(task, priority, due_date):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task, priority, due_date, completed) VALUES (?, ?, ?, 0)', (task, priority, due_date))
    conn.commit()
    conn.close()
    print("Task added successfully.")

def remove_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task removed successfully.")

def mark_task_completed(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("Task marked as completed.")

def list_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        print("List of Tasks:")
        for task in tasks:
            task_id, task_name, priority, due_date, completed = task
            status = "Completed" if completed else "Pending"
            print(f"Task ID: {task_id}, Task: {task_name}, Priority: {priority}, Due Date: {due_date}, Status: {status}")
    else:
        print("No tasks found.")

if __name__ == '__main__':
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Select an option (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter the task: ")
            priority = input("Enter the priority (high/medium/low): ")
            due_date = input("Enter the due date (YYYY-MM-DD): ")
            add_task(task, priority, due_date)
        elif choice == '2':
            task_id = input("Enter the task ID to remove: ")
            remove_task(task_id)
        elif choice == '3':
            task_id = input("Enter the task ID to mark as completed: ")
            mark_task_completed(task_id)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please select a valid option.")
