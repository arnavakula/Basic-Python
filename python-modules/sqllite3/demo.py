import sqlite3

'''
connection
cursor
execute sql function
commit if inserting data
fetchall if receiving data
'''

def create_table():
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def add(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO store VALUES(?, ?, ?)', (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM store')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM store WHERE item = ?', (name,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = sqlite3.connect('lite.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE store SET quantity = ?, price = ? WHERE item = ?', (quantity, price, item))
    conn.commit()
    conn.close()

delete('Wine Glass')
update('Table', 18, 50)
print(view())
