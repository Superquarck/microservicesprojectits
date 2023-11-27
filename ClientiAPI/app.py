from flask import Flask, jsonify
import psycopg2.pool
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname='UserDB',
    user='fede',
    password='mypassword',
    host='0.0.0.0',
    port='6000'
)

# API endpoint to retrieve data from the 'Clienti' table
@app.route('/api/clients', methods=['GET'])
def get_clients():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Select data from the 'Clienti' table
        select_query = "SELECT * FROM Clienti;"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Close the cursor (will return the connection to the pool) and commit changes
        cursor.close()
        connection.commit()

        # Convert the data to JSON and return it
        return jsonify({'clients': data})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
