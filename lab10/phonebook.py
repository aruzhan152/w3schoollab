import psycopg2
import csv

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="phonebook1",
    user="postgres",
    password="1234",
    port=5432
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

# Create a table to store PhoneBook entries
cur.execute('''CREATE TABLE IF NOT EXISTS phonebook1 (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                phone VARCHAR(255) NOT NULL
            )''')

# Function to insert data into the PhoneBook from a CSV file
def insert_data_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            cur.execute("INSERT INTO phonebook1 (name, phone) VALUES (%s, %s)", (row[0], row[1]))
            conn.commit()

# Function to insert data into the PhoneBook from console input
def insert_data_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("INSERT INTO phonebook1 (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()

# Function to update PhoneBook entry by name
def update_entry_by_name(name, new_name=None, new_phone=None):
    if new_name is None and new_phone is None:
        print("Please provide a new name or phone number.")
        return
    query = "UPDATE phonebook1 SET "
    if new_name is not None:
        query += f"name = '{new_name}', "
    if new_phone is not None:
        query += f"phone = '{new_phone}', "
    query = query[:-2] # remove trailing comma and space
    query += f"WHERE name = '{name}'"
    cur.execute(query)
    conn.commit()

# Function to update PhoneBook entry by phone number
def update_entry_by_phone(phone, new_name=None, new_phone=None):
    if new_name is None and new_phone is None:
        print("Please provide a new name or phone number.")
        return
    query = "UPDATE phonebook1 SET "
    if new_name is not None:
        query += f"name = '{new_name}', "
    if new_phone is not None:
        query += f"phone = '{new_phone}', "
    query = query[:-2] # remove trailing comma and space
    query += f"WHERE phone = '{phone}'"
    cur.execute(query)
    conn.commit()

# Function to query PhoneBook entries with a filter by name or phone number
def query_entries(filter=None, by_name=True):
    if filter is None:
        cur.execute("SELECT * FROM phonebook1")
    else:
        query = "SELECT * FROM phonebook1 WHERE "
        if by_name:
            query += f"name LIKE '{filter}%'"
        else:
            query += f"phone LIKE '{filter}%'"
        cur.execute(query)
    entries = cur.fetchall()
    for entry in entries:
        print(f"{entry[0]} | {entry[1]} | {entry[2]}")

# Function to delete PhoneBook entry by name
def delete_entry_by_name(name):
    cur.execute(f"DELETE FROM phonebook1 WHERE name = '{name}'")
    conn.commit()

# Function to delete PhoneBook entry by phone number
def delete_entry_by_phone(phone):
    cur.execute("DELETE FROM phonebook1 WHERE phone = %s", (phone,))
    conn.commit()

# Example usage of functions
insert_data_from_csv('phonebook1.csv')
insert_data_from_console()
update_entry_by_name('John Doe', new_name='Johnny')
update_entry_by_phone('555-1234', new_phone='555-5678')
query_entries('John')
delete_entry_by_name('Jane Doe')
delete_entry_by_phone('555-4321')

# Close the database connection and cursor
cur.close()
conn.close()