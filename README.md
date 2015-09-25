# lazy-todo
An implementation of a shared todo-list with command-line interface in Python.

## Config
Currently the following settings are to be configured in 'config.cfg':
### Database
- DB - The name of the database that will be used.
- Host - The host name of the database server.
- Port - The port of the database server.
### User
- Email - The email address of the current user

## Usage
### Creating a new task
Create a new task:
```
lazy new
```
Aliases:
```
lazy n
```
The user will then be prompted to enter the required information.
###  Deleting a task
To delete a task:
```
lazy delete <id of task>
```
Aliases:
```
lazy del <id of task>
lazy d <id of task>
```
### Inspecting a single task
To view information for a specific task:
```
lazy show <id of task>
```
Aliases:
```
lazy s <id of task>
```
### Viewing all tasks assigned to the current user
To get a list of all tasks, that are assigned to the current user:
```
lazy show
```
Aliases:
```
lazy s
```
### Importing tasks as JSON
To import a JSON file into the repository:
```
lazy import <path to file>
```
Aliases:
```
lazy imp <path of file>
```
### Exporting a task as JSON
To export a task as a JSON document:
```
lazy export <path of file> <id of task>
```
Aliases:
```
lazy exp <path of file> <id of task>
```
### Exporting all tasks of the current user as JSON
To export all tasks assigned to the current user:
```
lazy export <path of file>
```
Aliases:
```
lazy exp <path of file>
```
