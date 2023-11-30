import requests
import json
import unittest
from flask import Flask

class TestApiPrestiti(unittest.TestCase):
    url = ("http://127.0.0.1:4998/prestiti")

    def test_get_all_prestiti(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_prestiti_by_id(self):
        prestito_id = 1  
        response = requests.get(f"{self.url}/{prestito_id}")
        self.assertEqual(response.status_code, 200)
        

    def test_add_prestito(self):
        data = {
            'ID_clienti': 4,
            'ID_libri': 6,
            'Data_prestito': '2023-04-06',
            'Data_Restituzione': '2023-05-06'
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_prestiti(self):
        prestiti_id = 1  
        data = {
            'ID_clienti': 5,
            'ID_libri': 6,
            'Data_prestito': '2023-04-06',
            'Data_Restituzione': '2023-05-06'
        }
        response = requests.put(f"{self.url}/{prestiti_id}", json=data)
        self.assertEqual(response.status_code, 200)
        

    def test_delete_prestito(self):
        prestiti_id = 3 
        response = requests.delete(f"{self.url}/{prestiti_id}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
