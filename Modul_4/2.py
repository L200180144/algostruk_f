##-----------------------------NO. 2-----------------------------
def cariUangSakuTerkecil(kumpulan):
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
    return terkecil #kembalikan yang terkecil

print ("\n-----------------------------NO. 2-----------------------------")
print(cariUangSakuTerkecil(Daftar)) 

