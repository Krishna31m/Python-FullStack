import sqlite3

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

connection.commit()

def insert_user(name, email):
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    connection.commit()

def get_user():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def get_user_by_id(user_id):
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    return cursor.fetchone()

def update_user(user_id, name, email):
    cursor.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, user_id))
    connection.commit()
    print("User updated successfully.")

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connection.commit()
    print("User deleted successfully.")