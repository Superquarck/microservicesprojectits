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
    ('John', 'Doe', '123 Main St', 'City1'),
    ('Jane', 'Smith', '456 Oak St', 'City2'),
    ('Bob', 'Johnson', '789 Maple St', 'City3'),
    ('Eva', 'Garcia', '234 Cedar St', 'City7'),
    ('Frank', 'Taylor', '567 Spruce St', 'City8'),
    ('Grace', 'Martinez', '876 Oak St', 'City9'),
    ('Henry', 'Clark', '109 Walnut St', 'City10');
