#nomer 1
class manusia(object):
    """ clas manusia dengan inisiasi 'nama' """
    keadaan='lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucap(self):
        print("halo namaku: ",self.nama)
    def olah(self,k):
        print('saya habis',k)
        self.keadaan='lapar'
    def makan(self,s):
        print("saya baru saja makan ",s)
        self.keadaan='kenyang'
    def kali(self,n):
        return n*2

class mahasiswa(manusia):
    """ class mahsiswa yang dibangun dai class manusia """
    def __init__(self,nama,NIM,kota,us):
        self.Nama=nama
        self.NIM=NIM
        self.kota=kota
        self.us=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilin(self):
        return self.Nama
    def ambilnim(self):
        return self.NIM
    def ambiluang(self):
        return self.uang
    def makan(self,s):
        print ("saya makan",s)
        self.keadaan='kenyang'
    def pkota(self):
        return self.kota
    def perbarui(self,x):
        self.kota=x
    def tambah(self,x):
        self.uang=self.uang+x

class urut():
    def __init__(self, arr):
        self.arr = arr
        
    def mergeSort(self, arr): 
        if len(arr) >1: 
            mid = len(arr)//2 #Finding the mid of the array 
            L = arr[:mid] # Dividing the array elements  
            R = arr[mid:] # into 2 halves 
  
            self.mergeSort(L) # Sorting the first half 
            self.mergeSort(R) # Sorting the second half 
  
            i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    arr[k] = L[i] 
                    i+=1
                else: 
                    arr[k] = R[j] 
                    j+=1
                k+=1
          
        # Checking if any element was left 
            while i < len(L): 
                arr[k] = L[i] 
                i+=1
                k+=1
          
            while j < len(R): 
                arr[k] = R[j] 
                j+=1
                k+=1
    def printMerge(self, arr):
        print("hasil merge sort")
        self.mergeSort(arr)
        for i in range(len(arr)):         
            print(arr[i],end = " ") 
        print()
        print()
        
    def partition(self, arr,low,high): 
        i = ( low-1 )        
        pivot = arr[high]    
        for j in range(low , high): 
            if   arr[j] <= pivot: 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 
  
    def quickSort(self, arr,low,high): 
        if low < high: 
            pi = self.partition(arr,low,high) 
            self.quickSort(arr, low, pi-1) 
            self.quickSort(arr, pi+1, high) 

    def printQuick(self, arr):
        print("hasil quick sort")
        n = len(arr) 
        self.quickSort(arr,0,n-1) 
        for i in range(n): 
            print(arr[i],end=" ")
        print()
        print()

mh1 = mahasiswa("aaaa", 104, "qqqqq", 10000)
mh2 = mahasiswa("bbbb", 84, "wwwww", 13000)
mh3 = mahasiswa("cccc", 124, "eeeee", 5000)
mh4 = mahasiswa("dddd", 544, "rrrrr", 12000)
mh5 = mahasiswa("eeee", 4, "ttttt", 2000)

nimMH = [mh1.NIM, mh2.NIM, mh3.NIM, mh4.NIM, mh5.NIM]
usMH = [mh1.us, mh2.us, mh3.us, mh4.us, mh5.us]

a1 = urut(nimMH)
b2 = urut(usMH)

a1.printMerge(nimMH)
b2.printMerge(usMH)

a1.printQuick(nimMH)
b2.printQuick(usMH)
