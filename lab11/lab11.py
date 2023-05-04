import psycopg2
import csv
from config import host, user, password, db_name


def connection_to_db():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    return connection


def insert_data(conn_i):
    cursor_i = conn_i.cursor()

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    query_create_num = "INSERT INTO phonebook1 (name, phone) VALUES (%s, %s) RETURNING id;"

    cursor_i.execute(query_create_num, (name, phone))
    conn_i.commit()


def update_data(conn_u):
    cursor_u = conn_u.cursor()
    g = int(input("What do you want change phone - 1, name - 2: "))
    if g == 1:
        n = input("Enter your name to find you in DB: ")
        p = input("Enter your new phone number: ")
        query_update_num = "UPDATE phonebook1 SET phone = %s WHERE name = %s;"

        cursor_u.execute(query_update_num, (p, n))

    elif g == 2:
        n = input("Enter your phone number to find you in DB: ")
        p = input("Enter your new name number: ")
        query_update_num = "UPDATE phonebook1 SET name = %s WHERE phone = %s;"

        cursor_u.execute(query_update_num, (p, n))

    conn_u.commit()


def delete_data(conn_d):
    cursor_d = conn_d.cursor()
    phone = input("Enter your phone number to delete: ")
    cursor_d.execute("DELETE FROM phonebook1 WHERE phone = %s;", (phone,))
    conn_d.commit()


def get_data(conn_g):
    cursor_g = conn_g.cursor()
    i = int(input("Find by number - 1, find by name - 2: "))
    if i == 1:
        value = input("Enter phone number: ")
        cursor_g.execute("SELECT * from phonebook1 where phone = %s;", (value,))

    elif i == 2:
        value = input("Enter first name: ")
        cursor_g.execute("SELECT * from phonebook1 where name = %s;", (value,))

    conn_g.commit()
    results = cursor_g.fetchall()
    print(results)


def upload_from_csv(conn_f, path):
    cursor = conn_f.cursor()
    with open(path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cursor.execute("INSERT INTO phonebook1(name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn_f.commit()


conn = connection_to_db()
ch = int(input("Add new phone - 1, Update data - 2, Delete data - 3, Select Data - 4, upload data from csv file - 5: "))
path_to_file = "/Users/anara/git_tutorial/work/w3schoollab/lab11/phonebook1.csv"

if ch == 1:
    insert_data(conn)

elif ch == 2:
    update_data(conn)

elif ch == 3:
    delete_data(conn)

elif ch == 4:
    get_data(conn)

elif ch == 5:
    upload_from_csv(conn, path_to_file)


conn.close()