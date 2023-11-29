from flask import Flask, jsonify, request
import psycopg2.pool
from flask_cors import CORS
import time 

time.sleep(30)

app = Flask(__name__)
CORS(app)

# Create a connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    dbname='ClientiDB',
    user='fede',
    password='mypassword',
    host='clientidata',
    port='5432'
)

# API endpoint to retrieve data from the 'Clienti' table
@app.route('/clienti', methods=['GET'])
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
        return jsonify({'clienti': data})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

@app.route('/clienti', methods=['POST'])
def create_client():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        nome = request.json.get('Nome')
        cognome = request.json.get('Cognome')
        indirizzo = request.json.get('Indirizzo')
        citta = request.json.get('Citta')

        # Insert data into the 'Clienti' table
        insert_query = "INSERT INTO Clienti (Nome, Cognome, Indirizzo, Citta) VALUES (%s, %s, %s, %s) RETURNING *;"
        cursor.execute(insert_query, (nome, cognome, indirizzo, citta))
        new_client = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the new client data
        cursor.close()
        return jsonify({'clienti': new_client}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Update operation
@app.route('/clienti/id', methods=['PUT'])
def update_client(client_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        nome = request.json.get('Nome')
        cognome = request.json.get('Cognome')
        indirizzo = request.json.get('Indirizzo')
        citta = request.json.get('Citta')

        # Update data in the 'Clienti' table
        update_query = "UPDATE Clienti SET Nome = %s, Cognome = %s, Indirizzo = %s, Citta = %s, WHERE id = %s RETURNING *;"
        cursor.execute(update_query, (nome, cognome, indirizzo, citta, client_id))
        updated_client = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the updated client data
        cursor.close()
        return jsonify({'clienti': updated_client})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Delete operation
@app.route('/clienti/id', methods=['DELETE'])
def delete_client(client_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Delete data from the 'Clienti' table
        delete_query = "DELETE FROM Clienti WHERE id = %s RETURNING *;"
        cursor.execute(delete_query, (client_id,))
        deleted_client = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the deleted client data
        cursor.close()
        return jsonify({'clienti': deleted_client})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)