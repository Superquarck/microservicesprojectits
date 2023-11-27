from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection parameters
db_params = {
    'dbname': 'UserDB',
    'user': 'fede',
    'password': 'mypassword',
    'host': 'ContainerClienti',
    'port': '5432',
}

# API endpoint to retrieve data from the 'Clienti' table
@app.route('/api/clients', methods=['GET'])
def get_clients():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_params)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Select data from the 'Clienti' table
        select_query = "SELECT * FROM Clienti;"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Convert the data to JSON and return it
        return jsonify({'clients': data})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)