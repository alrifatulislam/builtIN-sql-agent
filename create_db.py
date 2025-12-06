import sqlite3

# Read SQL file
with open('Chinook_Sqlite.sql', 'r', encoding="utf-8") as f:
    sql_script = f.read()

# Create database and execute script
conn = sqlite3.connect("chinook.db")
conn.executescript(sql_script)
conn.close()
print("Database created successfully!")