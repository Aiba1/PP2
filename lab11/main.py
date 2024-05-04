import psycopg2
import csv
from config import host, user, password, db_name
from psycopg2 import Error
import re

conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
)
conn.autocommit = True

cursor = conn.cursor()


def createtable():
    sql = '''
        CREATE TABLE phone(
        name CHAR(20),
        number CHAR(12)
    )
    '''
    cursor.execute(sql)


def insertdata():
    name = input("Name to insert ")
    number = input("Number to insert ")
    sql = f'''
   INSERT INTO phone(name, number) VALUES
   ('{name}', '{number}')
'''
    cursor.execute(sql)

def insertfromcsv():
    with open("some.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            sql = f'''
                INSERT INTO phone(name, number) VALUES
                ('{row[0]}', '{row[1]}')
                '''
            cursor.execute(sql)


def updatedatabyname():
    find = input("Enter a name to find: ")
    update = input("Enter a new number: ")
    
    # Проверяем, есть ли запись с таким именем в базе данных
    cursor.execute(f"SELECT * FROM phone WHERE name = '{find}'")
    result = cursor.fetchone()
    
    if result:
        # Если запись существует, обновляем номер телефона
        sql = f"UPDATE phone SET number = '{update}' WHERE name = '{find}'"
    else:
        # Если запись не существует, добавляем новую запись
        sql = f"INSERT INTO phone(name, number) VALUES ('{find}', '{update}')"
        
    # Выполняем SQL-запрос
    cursor.execute(sql)


def updatedatabynumber():
    find = input("Enter a number to find ")
    update = input("Enter a new name ")
    sql = f'''
    UPDATE phone SET name = '{update}' WHERE number = '{find}'
    '''
    cursor.execute(sql)    
    
def deletedatabyname():
    find = input("Enter a name to delete ")
    sql = f'''
    DELETE FROM phone WHERE name = '{find}';
    '''
    cursor.execute(sql)
    
def deletedatabynumber():
    find = input("Enter a number to delete ")
    sql = f'''
    DELETE FROM phone WHERE number = '{find}';
    '''
    cursor.execute(sql)
    
def show():
    filter = input("What you need to find ")
    sql = f'''
    SELECT * FROM phone WHERE name LIKE '%{filter}%' OR number LIKE '%{filter}%'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        print('There are none')

def add_users():
    contacts = []
    incorrect_values = []
    pattern = r'^8777[0-9]{7}$|^8747[0-9]{7}$|^8778[0-9]{7}$|^8700[0-9]{7}$|^8707[0-9]{7}$|^8708[0-9]{7}$|^8705[0-9]{7}$|^8775[0-9]{7}$'
    
    num_contacts = int(input("Enter the number of contacts you want to add: "))
    
    for _ in range(num_contacts):
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts.append((name, number))
    
    try:
        for contact in contacts:
            if re.match(pattern, contact[1]):
                cursor.execute('INSERT INTO phone(name, number) VALUES (%s, %s)', (contact[0], contact[1]))
            else:
                incorrect_values.append(contact)
                
    except (Exception, Error) as error:
        print("ERROR:", error)
   
    print(f'List of incorrect values is: {incorrect_values}')
add_users()
# insertdata()
# deletedatabyname()
# deletedatabynumber()
# updatedatabyname()
# updatedatabynumber()
# show()
# add_users()

# Closing connection 
# conn.close()