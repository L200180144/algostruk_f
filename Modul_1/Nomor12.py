from random import*

x = randint(1, 100)
print("Permainan tebak angka.")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
while True :
    a = int(input("Masukan tebakan:>"))
    if a < x:
        print("tebakan anda terlalu kecil. Coba lagi")
    elif a > x:
        print("tebakan anda terlalu besar. Coba lagi")
    else :
        print("tebakan anda benar")
        break
