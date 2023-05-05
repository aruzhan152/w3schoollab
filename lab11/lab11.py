import psycopg2
import csv
from config import host, user, password, database

def connection_to_db():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

# Define the functions and stored procedures

def search_records(pattern, conn_a):
    # Define a function to search records based on a pattern
    print(f"Searching for pattern: {pattern}")
    cur_a = conn_a.cursor()
    cur_a.execute("SELECT * FROM phonebook1 WHERE name ILIKE %s OR phone ILIKE %s", (f"%{pattern}%", f"%{pattern}%"))
    rows = cur_a.fetchall()
    print(f"Found {len(rows)} rows matching the pattern.")
    for row in rows:
        print(row)

def insert_data(conn_b):
    cur_b = conn_b.cursor()

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    cur_b.execute("SELECT id FROM phonebook1 WHERE name=%s", (name,))
    result = cur_b.fetchone()
    if result is not None:
        # User exists, update phone
        user_id = result[0]
        cur_b.execute("UPDATE phonebook1 SET phone=%s WHERE id=%s", (phone, user_id))
        print(f"Phone number updated for user {name}.")
    else:
        # User does not exist, create new user
        cur_b.execute("INSERT INTO phonebook1 (name, phone) VALUES (%s, %s)", (name, phone))
        print(f"User {name} added to the phonebook1.")
    conn_b.commit()


def insert_many_users(conn_c, user_data):
    # Define a stored procedure to insert many new users by list of name and phone
    cur_c = conn_c.cursor()
    incorrect_data = []
    for data in user_data:
        name = data[0]
        phone = data[1]
        if len(phone) != 8 or not phone.isdigit():
            # Invalid phone number, add to incorrect data list
            incorrect_data.append(data)
            continue
        cur_c.execute("SELECT id FROM phonebook1 WHERE name=%s", (name,))
        result = cur_c.fetchone()
        if result is not None:
            # User exists, update phone
            user_id = result[0]
            cur_c.execute("UPDATE phonebook1 SET phone=%s WHERE id=%s", (phone, user_id))
            print(f"Phone number updated for user {name}.")
        else:
            # User does not exist, create new user
            cur_c.execute("INSERT INTO phonebook1 (name, phone) VALUES (%s, %s)", (name, phone))
            print(f"User {name} added to the phonebook1.")
    conn_c.commit()
    return incorrect_data

def paginate_records(conn_d, limit, offset):
    # Define a function to query data from the tables with pagination
    cur_d = conn_d.cursor()
    cur_d.execute("SELECT COUNT(*) FROM phonebook1")
    total_count = cur_d.fetchone()[0]
    cur_d.execute("SELECT * FROM phonebook1 ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur_d.fetchall()
    for row in rows:
        print(row)
    print(f"Showing records {offset+1} to {offset+len(rows)} out of {total_count}.")


def delete_records(conn_e, username=None, phone=None):
    # Define a stored procedure to delete data from the tables by username or phone
    cur_e = conn_e.cursor()
    if username is not None:
        cur_e.execute("DELETE FROM phonebook1 WHERE name=%s", (username,))
        conn_e.commit()
        print(f"All records with name '{username}' have been deleted.")
    elif phone is not None:
        cur_e.execute("DELETE FROM phonebook1 WHERE phone=%s", (phone,))
    else:
        print("Error: Must provide either a username or phone number to delete.")
        return

    conn_e.commit()
    print("Record(s) deleted successfully.")


conn = connection_to_db()
ch = int(input("Pattern search - 1, insert/update data - 2, insert many users - 3, Select Data - 4, upload data from csv file - 5: "))

if ch == 1:
    k=str(input("enter with "))
    search_records(k, conn)

elif ch == 2:
    insert_data(conn)

elif ch == 3:
    dataa = []
    while True:
        entry = input("Enter name and phone number separated by a space (or 'quit' to stop): ")
        if entry.lower() == 'quit':
            break
        name, phone = entry.split()
        dataa.append((name, phone))
    insert_many_users(conn, dataa)

elif ch == 4:
    k=int(input("starting point"))
    g=int(input("ending point"))
    paginate_records(conn, k, g)

elif ch == 5:
    k=int(input("by name - 1, by phone= 2 "))
    if k==1:
        g=str(input("Write with '' the name you're looking for "))
        delete_records(conn, username=g)
    else:
        g=str(input("Write with '' the phone you're looking for "))
        delete_records(conn, phone=g)

conn.close()