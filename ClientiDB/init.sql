-- Create a new database called 'UserDB'
CREATE DATABASE "UserDB";
\c "UserDB";

CREATE TABLE Clienti (

ID serial PRIMARY KEY,
Nome varchar(255),
Cognome varchar(255),
Indirizzo varchar(255),
Citta varchar(255)
);

INSERT INTO Clienti (Nome, Cognome, Indirizzo, Citta) VALUES
    ('John', 'Doe', '123 Main St', 'City1'),
    ('Jane', 'Smith', '456 Oak St', 'City2'),
    ('Bob', 'Johnson', '789 Maple St', 'City3'); 
