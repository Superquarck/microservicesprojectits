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
    dbname='LibriDB',
    user='fede',
    password='mypassword',
    host='libridata',
    port='5432'
)

#configurazione iniziale del logging
logging.basicConfig(level=logging.INFO,
filename="Libri.log",
filemode="w",
format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Connessione al Database dei Libri, riuscita con successo!")

# API endpoint to retrieve data from the 'Libri' table
@app.route('/libri', methods=['GET'])
def get_books():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Select data from the 'Libri' table
        select_query = "SELECT * FROM Libri;"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Close the cursor (will return the connection to the pool) and commit changes
        cursor.close()
        connection.commit()

        # Convert the data to JSON and return it
        return jsonify({'libri': data})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

@app.route('/libri', methods=['POST'])
def create_books():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        id_libri = request.json.get('ID_libri')
        titolo = request.json.get('Titolo')
        editore = request.json.get('Editore')
        genere = request.json.get('Genere')
        autore = request.json.get('Autore')

        # Insert data into the 'Libri' table
        insert_query = "INSERT INTO Libri (ID_libri, Titolo, Editore, Genere, Autore) VALUES (%s, %s, %s, %s, %s) RETURNING *;"
        cursor.execute(insert_query, (id_libri, titolo, editore, genere, autore))
        new_book = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the new client data
        cursor.close()
        return jsonify({'libri': new_book}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Update operation
@app.route('/libri/<int:libri_id>', methods=['PUT'])
def update_books(libri_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        titolo = request.json.get('Titolo')
        editore = request.json.get('Editore')
        genere = request.json.get('Genere')
        autore = request.json.get('Autore')

        # Update data in the 'Libri' table
        update_query = "UPDATE Libri SET Titolo = %s, Editore = %s, Genere = %s, Autore = %s WHERE id = %s RETURNING *;"
        cursor.execute(update_query, (titolo, editore, genere, autore, libri_id))
        update_book = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the updated client data
        cursor.close()
        return jsonify({'libri': update_book})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Delete operation
@app.route('/clienti/<int:libri_id>', methods=['DELETE'])
def delete_books(libri_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Delete data from the 'Clienti' table
        delete_query = "DELETE FROM Clienti WHERE id_libri = %s RETURNING *;"
        cursor.execute(delete_query, (libri_id,))
        deleted_book = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the deleted client data
        cursor.close()
        return jsonify({'libri': deleted_book})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4999)

logging.warning("Run dell'applicazione Libri")