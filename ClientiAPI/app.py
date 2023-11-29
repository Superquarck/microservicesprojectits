from flask import Flask, jsonify, request
import psycopg2.pool
from flask_cors import CORS
import time 
import logging
import json


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

#configurazione iniziale del logging
logging.basicConfig(level=logging.INFO,
filename="Clienti.log",
filemode="w",
format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Connessione al Database dei Clienti, riuscita con successo!")

# API endpoint to retrieve data from the 'Clienti' table
@app.route('/clienti', methods=['GET'])
def get_clienti():
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
def create_clienti():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        id = request.json.get('ID')
        nome = request.json.get('Nome')
        cognome = request.json.get('Cognome')
        indirizzo = request.json.get('Indirizzo')
        citta = request.json.get('Citta')

        # Insert data into the 'Clienti' table
        insert_query = "INSERT INTO Clienti (ID, Nome, Cognome, Indirizzo, Citta) VALUES (%s, %s, %s, %s, %s) RETURNING *;"
        cursor.execute(insert_query, (id, nome, cognome, indirizzo, citta))
        new_cliente = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the new client data
        cursor.close()
        return jsonify({'clienti': new_cliente}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Update operation
@app.route('/clienti/<int:clienti_id>', methods=['PUT'])
def update_clienti(clienti_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        nome = request.json.get('Nome')
        cognome = request.json.get('Cognome')
        indirizzo = request.json.get('Indirizzo')
        citta = request.json.get('Citta')

        # Update data in the 'Clienti' table
        update_query = "UPDATE Clienti SET Nome = %s, Cognome = %s, Indirizzo = %s, Citta = %s WHERE id = %s RETURNING *;"
        cursor.execute(update_query, (nome, cognome, indirizzo, citta, clienti_id))
        updated_cliente = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the updated client data
        cursor.close()
        return jsonify({'clienti': updated_cliente})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Delete operation
@app.route('/clienti/<int:clienti_id>', methods=['DELETE'])
def delete_clienti(clienti_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Delete data from the 'Clienti' table
        delete_query = "DELETE FROM Clienti WHERE id = %s RETURNING *;"
        cursor.execute(delete_query, (clienti_id,))
        deleted_cliente = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the deleted client data
        cursor.close()
        return jsonify({'clienti': deleted_cliente})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

logging.warning("Run dell'applicazione Clienti")