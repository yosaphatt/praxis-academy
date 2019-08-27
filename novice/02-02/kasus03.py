import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO') #mengecek nilai apakah sama atau tidak

    def test_isupper(self): 
        self.assertTrue('FOO'.isupper())  #mengecek nilai benar
        self.assertFalse('Foo'.isupper()) #mengecek nilai salah

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # memeriksa apakah s.split gagal ketika pemisah bukan string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()