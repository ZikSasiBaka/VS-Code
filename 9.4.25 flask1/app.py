from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)


def get_db_connection():
    return sqlite3.connect("mydb.db")


def create_table_cities():
    # Connect to SQLite database
    with get_db_connection() as connection:
        print("Connected to database mydb")
        cursor = connection.cursor()
        # Create table cities
        sql = '''
        CREATE TABLE IF NOT EXISTS cities (
            city_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        '''
        cursor.execute(sql)
        cursor.close()
        print("Database and table created successfully")


create_table_cities()
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Flask server!',
        'status': 'success'
    })
@app.route('/api/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Server is running'
    })


@app.route('/details')
def details():
    return jsonify({
        'firstname': 'oren',
        'lastname': 'davidi'
    })


@app.route('/cities', methods=['POST'])
def create_city():
    data = request.get_json()
    print(data)
    with get_db_connection() as connection:
        print("Connected to database mydb")
        cursor = connection.cursor()
        sql = 'INSERT INTO cities (name) VALUES (?)'
        cursor.execute(sql, (data['name'],))
        city_id = cursor.lastrowid
        connection.commit()
        cursor.close()
    return jsonify({
        'id': city_id,
        'name': data['name']
    })
# Get all cities
@app.route('/cities', methods=['GET'])
def get_cities():
    with get_db_connection() as connection:
        print("Connected to database mydb")
        cursor = connection.cursor()
        sql = 'SELECT * FROM cities'
        cursor.execute(sql)
        cities = cursor.fetchall()
        cursor.close()
    return jsonify({'cities': [dict(id=city[0], name=city[1]) for city in cities]})

# Delete city
@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    conn = sqlite3.connect('cities.db')
    
    # Check if city exists
    city = conn.execute('SELECT * FROM cities WHERE city_id = ?', (city_id,)).fetchone()
    if city is None:
        conn.close()
        return jsonify({'error': 'City not found'}), 404
    
    conn.execute('DELETE FROM cities WHERE city_id = ?', (city_id,))
    conn.commit()
    conn.close()
    
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
