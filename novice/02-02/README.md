# Unit Testing
Testing adalah proses untuk memastikan bahwa kode yang ditulis sudah beralan dengan seharusnya. Tujuan ini dapat dicapai dengan berbagai cara mulai dari secara manual memasukkan beberapa nilai dan memastikan hasil yang didapat sudah benar, hingga membuat serangkaian tes terstruktur yang berjalan secara otomatis dan memastikan bahwa kesuluruhan program sudah berjalan dengan seharusnya.

## Penjelasan kode program yg dibuat
### 1
    def tambah(x,y): #fungsional
        return x + y #mengembalikan nilai x ditambah y

    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(tambah(3,4), 8) #mengecek apakah nilai benar atau tidak

### 2

    def tambah(self):
        self.assertEqual(tambah([1, 2, 3]), 6, "Should be 6") #mengecek nilai apakah sama atau tidak

    def tambah_tuple(self): 
        self.assertEqual(tamabah((1, 2, 2)), 6, "Should be 6") #mengecek nilai apakah sama atau tidak

### 3
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
### 4
    class Mytest(unittest.TestCase):
	def test(self):
		self.assertEqual(p1.age, 46) #mengecek apakah memiliki nilai yang sama 
