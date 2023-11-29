-- Connect to the existing database (replace "UserDB" with your actual database name)
\c "PrestitiDB";

-- Create the "Prestiti" table
CREATE TABLE IF NOT EXISTS Prestiti (
    ID serial PRIMARY KEY,
    ID_Libri REFERENCES Libri(ID),
    ID_Clienti REFERENCES Clienti(ID),
    Data_prestito DATE,
    Data_restituzione DATE
);

-- Insert data into the "Prestiti" table
INSERT INTO Prestiti (ID_Libri, ID_Clienti, Data_prestito, Data_restituzione) VALUES
    ('2023-10-1', '2023-10-31'),
    ('2023-11-10', '2023-12-10'),
    ('2023-5-25', '2023-6-24');
