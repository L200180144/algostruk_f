from Latihan23 import Manusia
class SiswaSMA(Manusia):
    """class SiswaSMA yang dibangun dari class Manusia."""
    def __init__(self, nis, nama, kelas):
        self.nis = nis
        self.nama = nama
        self.kelas = kelas
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nis) \
            +' adalah siswa kelas '+self.kelas
        return s
    
    def ambilNis(self):
        return self.nis
    def ambilNama(self):
        return self.nama
    def ambilKelas(self):
        return self.kelas

nis = input("Masukkan NIS : ")
nama = input("Masukkan Nama : ")
kelas = input("Masukkan Kelas : ")
S1 = SiswaSMA(nis,nama,kelas)
