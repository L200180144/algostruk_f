class Pesan(object):
    """
        Sebuah class bernama pesan.
        Untuk memahami konsep Class dan Object.
    """
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumlahKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai ",len(self.teks)," karakter.")
    def perbarui(self, stringBaru):
        self.teks = stringBaru

    def apakahTerkandung(self, kata):
        self.kata = str(kata)
        if kata in self.teks:
            print("True")
        else:
            print("False")

    def hitungKonsonan(self):
        huruf = 'aiueoAIUEO'
        i = 0
        for j in self.teks:
            if j not in huruf:
                i+=1
        return (i)
    def hitungVokal(self):
        huruf = 'aiueoAIUEO'
        i = 0
        for j in self.teks:
            if j in huruf:
                i+=1
        return (i)

P1 = Pesan("Indonesia adalah negeri yang indah")
P1.apakahTerkandung("ege")
print(P1.hitungKonsonan())
print(P1.hitungVokal())
