##-----------------------------NO. 4-----------------------------
def cariKurangDari(kumpulan):
    b = []  
    for i in kumpulan:
        if i.uangSaku < 250000:
            terkecil = i.uangSaku
            b.append(kumpulan.index(i))
    return b

print ("\n-----------------------------NO. 4-----------------------------")
print(cariKurangDari(Daftar)) 
