-- Connect to the existing database (replace "UserDB" with your actual database name)
\c "LibriDB";

-- Create the "Clienti" table
CREATE TABLE IF NOT EXISTS Clienti (
    ID serial PRIMARY KEY,
    Titolo varchar(255),
    Editore varchar(255),
    Genere varchar(255),
    Autore VARCHAR(255)
);

-- Insert data into the "Clienti" table
INSERT INTO Clienti (ID, Titolo, Editore, Genere, Autore) VALUES
    ('1', 'La via del massacro', 'Mondadori', 'Thriller', 'Io'),
    ('2', 'Tre uomini e una gamba', 'Feltrinelli', 'Horror', 'Tu'),
    ('3', 'Dio', 'Mondadori', 'Horror', 'Loro');
