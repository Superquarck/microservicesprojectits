import requests
import json
import unittest
from flask import Flask

class TestApiLibri(unittest.TestCase):
    url = ("http://127.0.0.1:4999/libri")

    def test_get_all_books(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code, 200)
        
        
    def test_get_book_by_id(self):
        book_id = 1  
        response = requests.get(f"{self.url}/{book_id}")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected behavior of your API

    def test_add_book(self):
        data = {
            'titolo': 'Test Book',
            'autore': 'Test Author',
            'editore': 'Test Editor',
            'genere': 'Test Genere'
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        book_id = 1  
        data = {
            'titolo': 'Updated Test Book',
            'autore': 'Updated Test Author',
            'editore': 'Updated Editor',
            'genere': 'Updated Genere'
        }
        response = requests.put(f"{self.url}/{book_id}", json=data)
        self.assertEqual(response.status_code, 200)
        

    def test_delete_book(self):
        book_id = 3 
        response = requests.delete(f"{self.url}/{book_id}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()
