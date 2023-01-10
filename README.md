# To-Do App

This is a simple To-Do application created using Flask and SQLite. It allows users to add new tasks to the list and mark tasks as completed.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* Python 3.x installed on your system.
* SQLite3
* Flask

### Installing

* Clone the repository
```
$ git clone https://github.com/[your_username]/todo-app.git
```
* Install the dependencies
```
$ pip install -r requirements.txt
```
* Run the application 
```
$ python main.py
```
* Open `http://localhost:5000` in your browser

### Usage

The main page displays the list of pending tasks. You can add new tasks using the form at the bottom of the page. To mark a task as completed, click on the "Mark as completed" link on the right of the task.

### Troubleshooting

If you are running into issues with the application, here are a few things you can check:

* Make sure that the `tasks.db` file exists in the project directory. If it doesn't, create it.
* Verify that the database file name is correct in the code of your application.
* Verify that the code is trying to access the `tasks` table in the correct database.
* Verify that your database is being opened and closed properly in the code of your application.