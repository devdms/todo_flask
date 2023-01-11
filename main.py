from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from sqlite3 import Error

app = Flask(__name__,template_folder='templates',static_folder='static')

# Connect to the database
def connect_db():
    try:
        conn = sqlite3.connect('tasks.db')
        return conn
    except Error as e:
        print(e)

# Show the list of tasks
@app.route('/')
def show_tasks():
    # Connect to the database
    conn = connect_db()
    c = conn.cursor()

    # Select all pending tasks from the database
    c.execute("SELECT * FROM tasks WHERE status='pending'")
    tasks = c.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML page with the list of tasks
    return render_template('show_tasks.html', tasks=tasks)

# Add a new task
@app.route('/add_task', methods=['POST'])
def add_task():
    # Get the data from the form
    task_name = request.form.get('task_name', None)

    # Connect to the database
    conn = connect_db()
    c = conn.cursor()

    # Input validation 
    if task_name and task_name.strip():
        # Insert the new task into the database
        c.execute("INSERT INTO tasks (task_name, status) VALUES (?, 'pending')", (task_name,))

        # Save changes to the database
        conn.commit()
    else:
        # Return error message if task name is empty
        return "Task name is required", 400

    # Close the database connection
    conn.close()

    # Redirect the user to the main page
    return redirect(url_for('show_tasks'))

# Mark a task as completed
@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    # Connect to the database
    conn = connect_db()
    c = conn.cursor()

    # Input validation
    if task_id:
        # Update the task status to "completed" in the database
        c.execute("UPDATE tasks SET status='completed' WHERE task_id=?", (task_id,))

        # Save changes to the database
        conn.commit()
    else:
        # Return error message if task_id is not provided
        return "Task id is required", 400

    # Close the database connection
    conn.close()

    # Redirect the user to the main page
    return redirect(url_for('show_tasks'))

#Export tasks to a text file
@app.route('/export_tasks')
def export_tasks():
    # Connect to the database
    conn = connect_db()
    c = conn.cursor()

    # Select all tasks from the database
    c.execute("SELECT task_name FROM tasks")
    tasks = c.fetchall()

    # Close the database connection
    conn.close()

    # Create the text file
    task_file = '\n'.join([task[0] for task in tasks])

    # Create a response object with the text file
    response = make_response(task_file)

    # Set the headers to indicate that this is a text file
    response.headers["Content-Disposition"] = "attachment; filename=tasks.txt"
    response.headers["Content-type"] = "text/plain"

    return response

if __name__ == '__main__':
    app.run(debug=True)
