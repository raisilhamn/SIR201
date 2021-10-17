# A "Operator Overloading" tersedia di cpp dan python
import math


class Overloading:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num


a = Overloading(5)
b = Overloading(5)

print("Penjumlahan dengan operator overloading ",a + b)
print("Pengurangan dengan operator overloading ", a - b)

# B
# BendaBulat


class BendaBulat:
    def __init__(self, rad=None, h=None):
        self.rad = rad
        self.h = h

    def luasLingkaran(self):
        if self.rad != None:
            return math.pow(self.rad, 2)*math.pi
        else:
            kosong = "tidak ada variabel jari jari"
            return kosong

    def volumeBola(self):
        if self.rad != None:
            return math.pow(self.rad, 3)*math.pi*(4/3)
        else:
            kosong = "tidak ada variabel jari jari"
            return kosong

    def luasPermukaanTabung(self):
        if self.rad != None and self.h != None:
            return 2*math.pi*self.rad*(self.rad+self.h)
        elif self.rad == None:
            kosong = "tidak ada variabel jari jari"
            return kosong
        else:
            kosong = "tidak ada variabel tinggi"
            return kosong

    def volumeSilinder(self):
        if self.rad != None and self.h != None:
            return math.pi*self.rad*self.rad*self.h
        elif self.rad == None:
            kosong = "tidak ada variabel jari jari"
            return kosong
        else:
            kosong = "tidak ada variabel tinggi"
            return kosong


print("--------")
a = BendaBulat()
print("Luas lingkaran :", a.luasLingkaran())
print("Volume Bola : ", a.volumeBola())
print("Luas Permukaan tabung : ", a.luasPermukaanTabung())
print("Volume tabung : ", a.volumeSilinder())
print("--------")
b = BendaBulat(7)
print("Luas lingkaran :", b.luasLingkaran())
print("Volume Bola : ", b.volumeBola())
print("Luas Permukaan tabung : ", b.luasPermukaanTabung())
print("Volume tabung : ", b.volumeSilinder())
print("--------")
c = BendaBulat(7, 14)
print("Luas lingkaran :", c.luasLingkaran())
print("Volume Bola : ", c.volumeBola())
print("Luas Permukaan tabung : ", c.luasPermukaanTabung())
print("Volume tabung : ", c.volumeSilinder())


# B BendaSegiEmpat
class BendaSegiEmpat:
    def __init__(self, panjang=None, lebar=None, tinggi=None):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def luasBujurSangkar(self):
        if self.panjang != None:
            return "{:.5f}".format(float(math.pow(self.panjang, 2)))
        else:
            kosong = "tidak ada variabel panjang"
            return kosong

    def volumeKubus(self):
        if self.panjang != None:
            return "{:.5f}".format(float(math.pow(self.panjang, 3)))
        else:
            kosong = "tidak ada variabel panjang"
            return kosong

    def luasPersegiPanjang(self):
        if self.panjang != None and self.lebar != None:
            return "{:.5f}".format(float(self.panjang*self.lebar))
        elif self.panjang == None:
            kosong = "tidak ada variabel panjang"
            return kosong
        else:
            kosong = "tidak ada variabel lebar"
            return kosong

    def volumeBalok(self):
        if self.panjang != None and self.lebar != None and self.tinggi != None:
            return "{:.5f}".format(float(self.panjang * self.lebar * self.tinggi))
        elif self.panjang == None:
            kosong = "tidak ada variabel panjang"
            return kosong
        elif self.tinggi == None:
            kosong = "tidak ada variabel tinggi"
            return kosong
        elif self.lebar == None:
            kosong = "tidak ada variabel lebar"
            return kosong


print("--------")
a = BendaSegiEmpat(4)
print("Luas bujur sangkar : ", a.luasBujurSangkar())
print("volume kubus: ", a.volumeKubus())
print("Luas persegi panjang: ", a.luasPersegiPanjang())
print("Volume balok: ", a.volumeBalok())
print("--------")
a = BendaSegiEmpat(3, 5)
print("Luas bujur sangkar : ", a.luasBujurSangkar())
print("volume kubus: ", a.volumeKubus())
print("Luas persegi panjang: ", a.luasPersegiPanjang())
print("Volume balok: ", a.volumeBalok())
print("--------")
a = BendaSegiEmpat(3, 5, 7)
print("Luas bujur sangkar : ", a.luasBujurSangkar())
print("volume kubus: ", a.volumeKubus())
print("Luas persegi panjang: ", a.luasPersegiPanjang())
print("Volume balok: ", a.volumeBalok())


class Vektor:
    def __init__(self, *args):
        self.data = list(args)

    def jumlah2Vektor(self, a=None):
        if a != None:
            res = []
            for i in range(len(self.data)):
                tmp = a.data[i]+self.data[i]
                res.append(tmp)
            return res
        else:
            res = []
            for i in range(len(self.data)):
                tmp = self.data[i]+self.data[i]
                res.append(tmp)
            return res

    def selisih2Vektor(self, a=None):
        if a != None:
            res = []
            for i in range(len(self.data)):
                tmp = a.data[i]-self.data[i]
                res.append(tmp)
            return res
        else:
            res = []
            for i in range(len(self.data)):
                tmp = self.data[i]-self.data[i]
                res.append(tmp)
            return res

    def tampilVektor(self):
        return self.data


print("--------")
v1 = Vektor(3, 2, 1, 0)
v2 = Vektor(1, 3, 5, 7)
print(f"Vektor 1 = {v1.tampilVektor()}")
print(f"Vektor 2 = {v2.tampilVektor()}")
print(f"Jumlah Vektor 1 dan 2 = {v1.jumlah2Vektor(v2)}")
print(f"Jumlah Vektor 1 dan Vektor 1 = {v1.jumlah2Vektor()}")
print(f"Selisih Vektor 1 dan Vektor 2 = {v1.selisih2Vektor(v2)}")
print(f"Selisih Vektor 1 dan Vektor 1 = {v1.selisih2Vektor()}")
