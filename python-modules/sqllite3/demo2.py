import psycopg2

'''
connection
cursor
execute sql function
commit if inserting data
fetchall if receiving data
'''

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='vreck479don' host='localhost' port='5434'")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def add(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='vreck479don' host='localhost' port='5434'")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO store VALUES(%s, %s, %s)', (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='vreck479don' host='localhost' port='5434'")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM store')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(name):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='vreck479don' host='localhost' port='5434'")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM store WHERE item = %s', (name,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='vreck479don' host='localhost' port='5434'")
    cursor = conn.cursor()
    cursor.execute('UPDATE store SET quantity = %s, price = %s WHERE item = %s', (quantity, price, item))
    conn.commit()
    conn.close()

update('Wine Glass', 18, 8.5)
print(view())