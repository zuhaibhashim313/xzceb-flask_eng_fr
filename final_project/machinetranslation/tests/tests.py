import unittest
from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_frenchToEnglishNull(self):
        self.assertNotEqual(french_to_english('None'), '   ') 
    def test_frenchToEnglishWord(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_englishToFrenchNull(self):
        self.assertNotEqual(english_to_french('None'), '   ') 
    def test_englishToFrenchWord(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

if __name__=='__main__':
	unittest.main()