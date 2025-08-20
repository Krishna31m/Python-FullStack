import sqlite3

# Create table if it doesn't exist
connection = sqlite3.connect('pythonfull.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS calculate (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    a INT,
    b INT,
    result INT
);
''')

connection.commit()
connection.close()

# ADD new record
def add(a, b, result):
    connection = sqlite3.connect('pythonfull.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO calculate (a, b, result) VALUES (?, ?, ?)", (a, b, result))
    connection.commit()
    connection.close()

# GET all records
def get_record():
    connection = sqlite3.connect('pythonfull.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM calculate")
    data = cursor.fetchall()
    connection.close()
    return data

# GET record by ID
def get_record_by_id(id):
    connection = sqlite3.connect('pythonfull.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM calculate WHERE id = {id}")
    data = cursor.fetchone()
    connection.close()
    return data

# DELETE record by ID
def delete_record_by_id(id):
    connection = sqlite3.connect('pythonfull.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM calculate WHERE id = {id}")
    if cursor.fetchone() is None:
        connection.close()
        return False
    else:
        cursor.execute(f"DELETE FROM calculate WHERE id = {id}")
        connection.commit()
        connection.close()
        return True

# UPDATE record by ID
def update_record_id(id, a, b, result):
    connection = sqlite3.connect('pythonfull.db')
    cursor = connection.cursor()
    cursor.execute(
        "UPDATE calculate SET a = ?, b = ?, result = ? WHERE id = ?",
        (a, b, result, id)
    )
    connection.commit()
    connection.close()













# import sqlite3

# connection = sqlite3.connect('pythonfull.db')
# cursor = connection.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS calculate (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     a INT,
#     b INT,
#     result INT
# );
# ''')

# connection.commit()


# def get_getrecord():
#     connection = sqlite3.connect('pythonfull.db')
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM data")
#     data = cursor.fetchall()
#     connection.close()
#     return data


# def get_record_by_id(id):
#     connection = sqlite3.connect('pythonfull.db')
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM data where id={id}")
#     data = cursor.fetchone()
#     connection.close()
#     return data

# def delete_record_by_id(id):
#     connection = sqlite3.connect('pythonfull.db')
#     cursor = connection.cursor()
#     cursor.execute(f"SELECT * FROM data where id = {id}")
#     if cursor.fetchone() is None:
#         connection.close()
#         return False
#     else:
#         cursor.execute(f"DELETE FROM data where id = {id}")
    
