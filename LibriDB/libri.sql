-- Connect to the existing database (replace "UserDB" with your actual database name)
\c "LibriDB";

-- Create the "Libri" table
CREATE TABLE IF NOT EXISTS Libri (
    ID serial PRIMARY KEY,
    Titolo varchar(255),
    Editore varchar(255),
    Genere varchar(255),
    Autore VARCHAR(255)
);

-- Insert data into the "Libri" table
INSERT INTO Libri (Titolo, Editore, Genere, Autore) VALUES
    ('La via del massacro', 'Mondadori', 'Thriller', 'Io'),
    ('Tre uomini e una gamba', 'Feltrinelli', 'Horror', 'Tu'),
    ('Dio', 'Mondadori', 'Horror', 'Loro');
