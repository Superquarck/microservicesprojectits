-- Connect to the existing database (replace "UserDB" with your actual database name)
\c "ClientiDB";

-- Create the "Clienti" table
CREATE TABLE IF NOT EXISTS Clienti (
    ID serial PRIMARY KEY,
    Nome varchar(255),
    Cognome varchar(255),
    Indirizzo varchar(255),
    Citta varchar(255)
);

-- Insert data into the "Clienti" table
INSERT INTO Clienti (Nome, Cognome, Indirizzo, Citta) VALUES
    ('Alice', 'Brown', '321 Elm St', 'City4'),
    ('Charlie', 'Miller', '654 Pine St', 'City5'),
    ('David', 'Davis', '987 Birch St', 'City6'),
    ('Eva', 'Garcia', '234 Cedar St', 'City7'),
    ('Frank', 'Taylor', '567 Spruce St', 'City8'),
