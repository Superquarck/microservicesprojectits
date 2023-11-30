import requests
import json
import unittest
from flask import Flask

class TestApiClienti(unittest.TestCase):
    url = ("http://127.0.0.1:5000/clienti")

    def test_get_all_clienti(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_clienti_by_id(self):
        clienti_id = 1  
        response = requests.get(f"{self.url}/{clienti_id}")
        self.assertEqual(response.status_code, 200)
        

    def test_add_clienti(self):
        data = {
            'Nome': 'Test Nome',
            'Cognome': 'Test Cognome',
            'Indirizzo': 'Test Indirizzo',
            'Citta': 'Test Citta'
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_clienti(self):
        clienti_id = 1  
        data = {
            'Nome': 'Updated Nome',
            'Cognome': 'Updated Cognome',
            'Indirizzo': 'Updated Indirizzo',
            'Citta': 'Updated Citta'
        }
        response = requests.put(f"{self.url}/{clienti_id}", json=data)
        self.assertEqual(response.status_code, 200)
        

    def test_delete_clienti(self):
        clienti_id = 3 
        response = requests.delete(f"{self.url}/{clienti_id}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
