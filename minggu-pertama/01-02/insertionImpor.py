def InsertionSort(val):
   for index in range(1,len(val)): #memasukan nilai variabel val ke index
     valueaktif = val[index] #persamaan 
     posisi = index #persamaan 
 
     while posisi>0 and val[posisi-1]>valueaktif: #perulangan
         val[posisi]=val[posisi-1] 
         posisi = posisi-1
 
     val[posisi]=valueaktif
