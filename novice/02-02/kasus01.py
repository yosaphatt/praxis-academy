import unittest

def tambah(x,y): #fungsional
    return x + y #mengembalikan nilai x ditambah y

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(tambah(3,4), 8) #mengecek apakah nilai benar atau tidak

if __name__ == '__main__':
    unittest.main()