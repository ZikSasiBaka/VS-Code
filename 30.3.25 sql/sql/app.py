import sqlite3  # Add SQLite import


def print_tblPersons():
    # Connect to SQLite database
    connection = sqlite3.connect('python_db.db')
    print("Connected to database")


    cursor = connection.cursor()
    
    sql = "select * from tblPersons"

    cursor.execute(sql)
    tblPersons = cursor.fetchall() 


    for person in tblPersons:
        print(person)
  
    cursor.close() 
    connection.close()

print_tblPersons()

def create_table_cities():
    # Connect to SQLite database
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    # create table:
    sql = '''create table if not exists tblCities 
            (city_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            city_name Text not null)'''
    cursor.execute(sql)
    cursor.close()
    connection.close()
    print("table has been created successfully")

create_table_cities()

def insert_city(city_name):
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    sql = 'insert into tblCities(city_name) values(?)'
    cursor.execute(sql, (city_name,))
    connection.commit() # save
    cursor.close()
    connection.close()

# for i in range(3):
#     city = input("enter city name: ")
#     insert_city(city)

def insert_many_cities(city_names):
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    sql = 'insert into tblCities(city_name) values(?)'
    cursor.executemany(sql, city_names)
    connection.commit() # save
    cursor.close()
    connection.close()

sample_cities = [
    ('london',),
    ('amsterdam',),
    ('tokyo',),
    ('paris',),
    ('new york',),
]

# insert_many_cities(sample_cities) ---> crashes the code after this one
print("tables have been added successfully")

def select_by_city_id(city_id):
    # Connect to SQLite database
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    sql = 'select * from tblCities where city_id = ?'
    cursor.execute(sql, (city_id,))
    city = cursor.fetchone()
    print(city)
    connection.commit()
    cursor.close()
    connection.close()

select_by_city_id(3)

def delete_city_by_id(city_id):
    # Connect to SQLite database
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    sql = 'delete from tblCities where city_id = ?'
    cursor.execute(sql, (city_id,))
    city = cursor.fetchone()
    print(city)
    connection.commit()
    cursor.close()
    connection.close()

delete_city_by_id(6)

def update_city_by_id(city_id, new_name):
    # Connect to SQLite database
    connection = sqlite3.connect('python_db.db')
    print("Connected to database tblCities")

    cursor = connection.cursor()
    sql = 'update tblCities set city_name = ? where city_id = ?'
    cursor.execute(sql, (new_name, city_id,))
    city = cursor.fetchone()
    print(city)
    connection.commit()
    cursor.close()
    connection.close()

update_city_by_id(9, "kiriyat ono")