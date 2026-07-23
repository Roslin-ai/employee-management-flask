from flask import Flask, request, render_template, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/employees", methods = ["GET"])
def list_employees():
    success = request.args.get("success")
    delete = request.args.get("deleted")
    update = request.args.get("updated")
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute(" SELECT * FROM employees")

    rows = cursor.fetchall()
    result = []
    for row in rows:
        emp_dict = {"id": row[0], "name": row[1], "department": row[2], "salary": row[3]}
        result.append(emp_dict)
    conn.close()
    return render_template("employees.html", employees = result, success=success, deleted=delete, updated=update)

@app.route("/add_employee", methods = ["POST"])
def add_employee():
    name = request.form.get("emp_name")
    department = request.form.get("emp_department")
    salary = int(request.form.get("emp_salary"))
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?,?,?)", 
                   (name, department, salary))
    
    conn.commit()
    conn.close()
    return redirect("/employees?success=1")

@app.route("/delete_employee/<int:emp_id>", methods = ["POST"])
def delete_employee(emp_id):
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id= ?", (emp_id,))
    conn.commit()
    conn.close()                                                   
    return redirect("/employees?deleted=1")

@app.route("/update_employee/<int:emp_id>", methods = ["POST"])
def update_employee(emp_id):
    new_salary = int(request.form.get("new_salary"))
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET salary=? WHERE id=?", (new_salary, emp_id))
    conn.commit()
    conn.close()
    return redirect("/employees?updated=1")

if __name__ == "__main__":
    app.run(debug = True)