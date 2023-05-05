
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
    cur_a = conn_a.cursor()
    cur_a.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s", (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    rows = cur_a.fetchall()
    for row in rows:
        print(row)

def insert_data(conn_b):
    cur_b = conn_b.cursor()

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    cur_b.execute("SELECT id FROM phonebook WHERE name=%s", (name,))
    result = cur_b.fetchone()
    if result is not None:
        # User exists, update phone
        user_id = result[0]
        cur_b.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (phone, user_id))
        print(f"Phone number updated for user {name}.")
    else:
        # User does not exist, create new user
        cur_b.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
        print(f"User {name} added to the phonebook.")
    conn_b.commit()


def insert_many_users(conn_c):
    # Define a stored procedure to insert many new users by list of name and phone
    cur_c = conn_c.cursor()
    incorrect_data = []
    for data in conn_c:
        name = data[0]
        phone = data[1]
        if len(phone) != 10 or not phone.isdigit():
            # Invalid phone number, add to incorrect data list
            incorrect_data.append(data)
            continue
        cur_c.execute("SELECT id FROM phonebook WHERE name=%s", (name,))
        result = cur_c.fetchone()
        if result is not None:
            # User exists, update phone
            user_id = result[0]
            cur_c.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (phone, user_id))
            print(f"Phone number updated for user {name}.")
        else:
            # User does not exist, create new user
            cur_c.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
            print(f"User {name} added to the phonebook.")
    conn_c.commit()
    return incorrect_data

def paginate_records(limit, offset):
    # Define a function to query data from the tables with pagination
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM phonebook")
    total_count = cur.fetchone()[0]
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print(f"Showing records {offset+1} to {offset+len(rows)} out of {total_count}.")

def delete_records(username=None, phone=None):
    # Define a stored procedure to delete data from the tables by username or phone
    cur = conn.cursor()
    if username is not None:
        cur.execute("DELETE FROM phonebook WHERE name=%s", (username,))
        conn.commit()
        print(f"All records with name '{username}' have been deleted.")
    elif phone is not None:
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))
    else:
        print("Error: Must provide either a username or phone number to delete.")
        return

    conn.commit()
    print("Record(s) deleted successfully.")

conn = connection_to_db()

