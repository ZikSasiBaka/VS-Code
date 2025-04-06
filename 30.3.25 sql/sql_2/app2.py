import sqlite3

def create_table_workers():
    connection = sqlite3.connect('python_db2.db')
    print("connected to database successfully")

    cursor = connection.cursor()
    sql = '''create table if not exists tblWorkers
            (worker_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            salary NUMERIC NOT NULL,
            city_id INTEGER,
            FOREIGN KEY (city_id) REFERENCES city(id))'''
    cursor.execute(sql)
    cursor.close()
    connection.close()
    print("table has been successfully created!")

#create_table_workers()

def insert_new_worker(fname, lname, salary, city_id):
    connection = sqlite3.connect('python_db2.db')
    print("connected to database successfully")

    cursor = connection.cursor()
    sql = 'insert into tblWorkers(fname, lname, salary, city_id) values(?,?,?,?)'
    cursor.execute(sql, (fname, lname, salary, city_id,))
    connection.commit()
    cursor.close()
    connection.close()
# for i in range(5):
#     fname = input("enter first name: ")
#     lname = input("enter last name: ")
#     salary = input("enter salary: ")
#     city_id = input("enter city id: ")
#     insert_new_worker(fname, lname, salary, city_id)

def delete_by_id(worker_id):
    connection = sqlite3.connect('python_db2.db')
    print("connected to database successfully")

    cursor = connection.cursor()
    sql = 'delete from tblWorkers where worker_id = ?'
    cursor.execute(sql, (worker_id,))
    city = cursor.fetchone()
    print(city)
    connection.commit()
    cursor.close()
    connection.close()

# for i in range(2):
#     delete = int(input("delete worker id number: "))
#     delete_by_id(delete)

def create_table_cities():
    connection = sqlite3.connect('python_db2.db')
    print("connected to database successfully")

    cursor = connection.cursor()
    sql = '''create table if not exists tblCities
            (city_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL)'''
    cursor.execute(sql)
    cursor.close()
    connection.close()
    print("table has been successfully created!")

# create_table_cities()

def insert_new_city(city_name):
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = 'insert into tblCities(city_name) values(?)'
    cursor.execute(sql, (city_name,))
    connection.commit()
    cursor.close()
    connection.close()

# for i in range(3):
#     city = input("add city here: ")
#     insert_new_city(city)

def select_by_id(worker_id):
    connection = sqlite3.connect('python_db2.db')
    print("connected to database successfully")
    
    cursor = connection.cursor()
    sql = '''select fname, lname, salary, city_name
            from tblWorkers
            inner join tblCities on tblWorkers.city_id = tblCities.city_id
            where tblWorkers.worker_id = ?'''
    cursor.execute(sql, (worker_id,))
    worker = cursor.fetchone()
    print(worker)
    connection.commit()
    cursor.close()
    connection.close()
    
# for i in range(3):
#     worker = int(input("enter worker id: "))
#     select_by_id(worker)

def higher_salary(n):
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = '''select fname, lname, salary, city_name
            from tblWorkers
            inner join tblCities on tblWorkers.city_id = tblCities.city_id
            where salary > ?'''
    cursor.execute(sql, (n,))
    salary = cursor.fetchall()
    print(salary)
    connection.commit()
    cursor.close()
    connection.close()

# n = int(input("enter a number to show salary higher than it: "))
# higher_salary(n)

def lower_salary(n):
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = '''select fname, lname, salary, city_name
            from tblWorkers
            inner join tblCities on tblWorkers.city_id = tblCities.city_id
            where salary < ?'''
    cursor.execute(sql, (n,))
    salary = cursor.fetchall()
    print(salary)
    connection.commit()
    cursor.close()
    connection.close()

# n = int(input("enter a number to show salary lower than it: "))
# lower_salary(n)    

# select_by_id(7)
# higher_salary(6000)

def min_max_salary(min, max):
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = '''select fname, lname, salary, city_name
            from tblWorkers
            inner join tblCities on tblWorkers.city_id = tblCities.city_id
            where salary > ? and salary < ?'''
    cursor.execute(sql, (min, max,))
    salary = cursor.fetchall()
    print(salary)
    connection.commit()
    cursor.close()
    connection.close()

# min_max_salary(5000, 10000)
    
def amount_of_workers():
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = '''select count (*)
            from tblWorkers'''
    cursor.execute(sql)
    count = cursor.fetchall()
    print(count)
    connection.commit()
    cursor.close()
    connection.close()

# amount_of_workers()

def worker_info(fname, lname):
    connection = sqlite3.connect('python_db2.db')
    print("connection to database has been established")

    cursor = connection.cursor()
    sql = '''select fname, lname, city_name
            from tblWorkers
            inner join tblCities on tblWorkers.city_id = tblCities.city_id
            where fname = ? and lname = ?'''
    cursor.execute(sql, (fname, lname,))
    info = cursor.fetchall()
    print(info)
    connection.commit()
    cursor.close()
    connection.close()

# fname = input("enter worker first name for info: ")
# lname = input("enter worker last name for info: ")
# worker_info(fname, lname)