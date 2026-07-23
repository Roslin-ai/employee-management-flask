import sqlite3

conn = sqlite3.connect("employee.db")

conn.execute(""" 
             CREATE TABLE IF NOT EXISTS employees (
             id INTEGER PRIMARY KEY,
             name TEXT,
             department TEXT,
             salary INTEGER
    )
""")
conn.commit()
conn.close()