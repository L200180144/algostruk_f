##-----------------------------NO. 7-----------------------------
def binSearch(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low != high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            break
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data

List = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9]
elemen = 4

print ("\n-----------------------------NO. 7-----------------------------")
print ("Indeks lokasi elemen ", elemen, "yang terdapat pada list ", List, "yaitu ")
print (binSearch(List, elemen))
