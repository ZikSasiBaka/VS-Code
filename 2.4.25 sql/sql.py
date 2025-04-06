import sqlite3

class City:
    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name
    
    def __str__(self):
        return f"city_id: {self.city_id}, city_name: {self.city_name}"
    
    def create_table_cities(self):
        conn = sqlite3.connect('python_self.db')
        print("connection to database has been established")

        cursor = conn.cursor()
        sql = '''create table if not exists tblCities
                (city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                city_name Text not null)'''
        
        cursor.execute(sql)
        cursor.close()
        conn.close()
        print("table has been created successfully")
    
    def insert_into_table(self, city_name):
        conn = sqlite3.connect('python_self.db')
        print("connection to database has been established")
        if not isinstance(str):
            raise ValueError("please enter a city name!")

        cursor = conn.cursor()
        sql = 'insert into tblCities(city_name) values(?)'
        cursor.execute(sql, (city_name,))
        conn.commit()
        cursor.close()
        conn.close()
        print("data has been successfully added to table")



    
    