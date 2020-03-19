##-----------------------------NO. 3-----------------------------
def cariyangTerkecil(kumpulan):
    n = []  
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            n.append(kumpulan.index(i))
    return n

print ("\n-----------------------------NO. 3-----------------------------")
print(cariyangTerkecil(Daftar)) 
