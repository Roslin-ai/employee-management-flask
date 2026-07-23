# Employee Management App
     A simple full-stack web application built with Flask and SQLite to manage employee records. Supports full CRUD operations (Create, Read, Update, Delete) through a clean, form-based interface.

## Features

- **View all employees** — displays employee ID, name, department, and salary in a table
- **Add a new employee** — form-based entry with name, department, and salary
- **Update employee salary** — inline editing directly from the employee list
- **Delete an employee** — remove a record with a single click
- Success/confirmation messages after each action (add, update, delete)
- Persistent storage using SQLite — data survives server restarts

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML, Jinja2 templating

## Project Structure
    emp_management/
    ├── app.py # Main Flask application (routes)
    ├── emp_db.py # One-time script to set up the database and table
    ├── templates/
    │ └── employees.html # Employee list, add form, update/delete buttons
    └── .gitignore

## How to Run

1. **Clone this repository**
    git clone https://github.com/Roslin-ai/employee-management-flask.git
    cd employee-management-flask

2. **Install Flask**
    pip install flask

3. **Set up the database** (run once)
    python emp_db.py

4. **Run the app**
    python app.py

5. **Open your browser** and visit: http://127.0.0.1:5000/employees

## What I Learned
    This project was built while learning Flask fundamentals — routing, HTTP methods (GET/POST), Jinja2 templating, form handling, and connecting Flask to a SQLite database for persistent CRUD operations.