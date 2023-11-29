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
    dbname='PrestitiDB',
    user='fede',
    password='mypassword',
    host='prestitidata',
    port='5432'
)

#configurazione iniziale del logging
logging.basicConfig(level=logging.INFO,
filename="Utenti.log",
filemode="w",
format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Connessione al Database dei Clienti, riuscita con successo!")

# API endpoint to retrieve data from the 'Prestiti' table
@app.route('/prestiti', methods=['GET'])
def get_prestiti():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Select data from the 'Prestiti' table
        select_query = "SELECT * FROM Prestiti;"
        cursor.execute(select_query)
        data = cursor.fetchall()

        # Close the cursor (will return the connection to the pool) and commit changes
        cursor.close()
        connection.commit()

        # Convert the data to JSON and return it
        return jsonify({'prestiti': data})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

@app.route('/prestiti', methods=['POST'])
def create_prestiti():
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        data_prestito = request.json.get('Data_prestito')
        data_restituzione = request.json.get('Data_restituzione')

        # Insert data into the 'Prestito' table
        insert_query = "INSERT INTO Prestito (Data_prestito, Data_restituzione) VALUES (%s, %s) RETURNING *;"
        cursor.execute(insert_query, (data_prestito, data_restituzione))
        new_prestito = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the new client data
        cursor.close()
        return jsonify({'prestiti': new_prestito}), 201

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Update operation
@app.route('/prestiti/<int:prestiti_id>', methods=['PUT'])
def update_prestito(prestiti_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Extract data from the request
        data_prestito = request.json.get('Data_prestito')
        data_restituzione = request.json.get('Data_Restituzione')

        # Update data in the 'Prestiti' table
        update_query = "UPDATE Prestiti SET Data_Prestito %s, Data_Restituzione = %s WHERE id = %s RETURNING *;"
        cursor.execute(update_query, (data_prestito, data_restituzione, prestiti_id))
        update_prestito = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the updated client data
        cursor.close()
        return jsonify({'prestiti': update_prestito})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)

# Delete operation
@app.route('/prestiti/<int:prestiti_id>', methods=['DELETE'])
def delete_prestito(prestiti_id):
    connection = connection_pool.getconn()
    try:
        cursor = connection.cursor()

        # Delete data from the 'Prestiti' table
        delete_query = "DELETE FROM Prestiti WHERE id = %s RETURNING *;"
        cursor.execute(delete_query, (prestiti_id,))
        deleted_prestito = cursor.fetchone()

        # Commit changes
        connection.commit()

        # Close the cursor (will return the connection to the pool) and return the deleted client data
        cursor.close()
        return jsonify({'prestiti': deleted_prestito})

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        # Always return the connection to the pool
        connection_pool.putconn(connection)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4998)

logging.warning("Run dell'applicazione Libri")