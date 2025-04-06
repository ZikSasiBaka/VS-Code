import sqlite3
class City:
    def __init__(self, city_id, name):
        self.city_id = city_id
        self.name = name 

    def __str__(self):
        return (f"city_id:{self.city_id}, name:{self.name}" )

    def create_table_cities(self):
        # Connect to SQLite database
        connection = sqlite3.connect('python_self.db')
        print("Connected to database python_self.db")

        cursor = connection.cursor()
        #create table cities 
        sql = '''create table if not exists cities
                (city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name Text not null)
            '''
        cursor.execute(sql)
        cursor.close()
        connection.close() 
        print("Database and table created successfully")

    def insert(self, name):
        # Remove MySQL comment since we're using SQLite
        connection = sqlite3.connect('python_self.db')
        print("Connected to database python_self.db")

        cursor = connection.cursor()
        sql = 'insert into cities (name) values(?)'  
        cursor.execute(     sql ,  (name,)   )
        connection.commit()# save 
        cursor.close()
        connection.close()

    def select_by_id(self, id):
        # Remove MySQL comment since we're using SQLite
        connection = sqlite3.connect('python_self.db')
        print("Connected to database python_selfV2.db")
        cursor = connection.cursor()
        sql = 'select * from cities where city_id = ?'  
        cursor.execute(     sql,  (id,)   )
        city = cursor.fetchone()
        cursor.close()
        connection.close()
        return city 

    def delete_by_id(self, id):
        # Remove MySQL comment since we're using SQLite
        connection = sqlite3.connect('python_self.db')
        print("Connected to database python_self.db")
        cursor = connection.cursor()
        sql = 'delete  from cities where city_id = ?'  
        cursor.execute(     sql,  (id,)   )
        connection.commit() # save 
        cursor.close()
        connection.close()

    def update_by_id(self, id, new_name):
        # Remove MySQL comment since we're using SQLite
        connection = sqlite3.connect('python_self.db')
        print("Connected to database python_self.db")
        cursor = connection.cursor()
        sql = 'update cities set name = ? where city_id = ?'  
        cursor.execute(     sql,  (new_name,id,)   )
        connection.commit() # save 
        cursor.close()
        connection.close()


