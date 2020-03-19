##-----------------------------NO. 6-----------------------------
def binSe(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
        #Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

a = [2,3,5,6,8,9,10,11,12,13,14]
index_a = 12
index_b = 17

print ("\n-----------------------------NO. 6-----------------------------")
print ("Index :", index_a)
print (binSe(a, index_a))

print ("\nIndex :", index_b)
print (binSe(a, index_b))
