-- Connect to the existing database 
\c "PrestitiDB";

-- Create the "Prestiti" table
CREATE TABLE IF NOT EXISTS Prestiti (
    ID serial PRIMARY KEY,
    ID_Libri INT,
    ID_Clienti INT,
    Data_prestito DATE,
    Data_restituzione DATE
);

-- Insert data into the "Prestiti" table
INSERT INTO Prestiti (ID_Libri, ID_Clienti, Data_prestito, Data_restituzione) VALUES
    ('1', '2', '2023-10-01', '2023-10-31'),
    ('2', '1', '2023-11-10', '2023-12-10'),
    ('3', '1', '2023-05-25', '2023-06-24'),
    ('4', '3', '2023-07-01', '2023-07-31');
