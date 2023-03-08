import unittest
import os
import PyPDF2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from grobid_client.grobid_client import GrobidClient
import entrega

class TestMyCode(unittest.TestCase):

    # Prueba sin pdf accesible
    def test_getGrobid(self):
        pdf = ""
        respuesta= entrega.getGrobid(pdf)
        self.assertIsNone(respuesta)

    # Prueba comprobar abstracto  
    def test_getAbstract(self):
        respuesta = '<abstract>This is the abstract</abstract>'
        expected_output = b'This is the abstract'
        self.assertEqual(entrega.getAbstract(respuesta), expected_output)

    # Prueba Wordcloud de abstract vacío
    def test_getWordCloud(self):
        abstract =""
        respuesta= entrega.getWordCloud(abstract)
        self.assertIsNone(respuesta)

    # Prueba de numero de figuras
    def test_getNumFigures(self):
        respuesta = '<figure>This is a figure</figure><figure>This is another figure</figure>'
        expected_output = 2
        self.assertEqual(entrega.getNumFigures(respuesta), expected_output)

    # Prueba de numero de links
    def test_getLinks(self):
        respuesta = '<ptr target="link1"/>'
        expected_output = ['link1']
        self.assertEqual(entrega.getLinks(respuesta), expected_output)

if __name__ == '__main__':
    unittest.main()