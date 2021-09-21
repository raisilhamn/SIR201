# 1

import math


class BendaBulat:
    def luasLingkaran(radius):
        luas = math.pi * radius * radius
        return luas

    def volumeBola(radius):
        volume = (4/3) * math.pow(radius, 3) * math.pi
        return volume


class BendaBulatDua:
    def __init__(self, radius):
        self.radius = radius

    def luasLingkaran(self):
        luas = math.pi * self.radius * self.radius
        return luas

    def volumeBola(self):
        volume = (4/3) * math.pow(self.radius, 3) * math.pi
        return volume

    def getRadius(self):
        return self.radius

    def setRadius(self):
        rad = int(input("Masukan radius "))
        self.radius = rad


class bidangSegiEmpat:
    def luasBujurSangkar(sisi):
        luas = int(math.pow(sisi, 2))
        return luas

    def luasPersegiPanjang(panjang, lebar):
        luas = panjang * lebar
        return luas


class bidangSegiEmpatDua:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def luasBujurSangkar(self):
        luas = int(math.pow(self.panjang, 2))
        return luas

    def luasPersegiPanjang(self):
        luas = self.panjang * self.lebar
        return luas

    def getLebar(self):
        return self.lebar

    def getPanjang(self):
        return self.getPanjang

    def setPanjang(self):
        newPanjang = int(input("Masukkan panjang : "))
        self.panjang = newPanjang

    def setLebar(self):
        newLebar = int(input("Masukkan lebar : "))
        self.lebar = newLebar

    def setRadius(self):
        rad = int(input("Masukan radius "))
        self.radius = rad


print("nomor 1")
luas = BendaBulat.luasLingkaran(14)
print("luas lingkaran = ", luas)
volume = BendaBulat.volumeBola(14)
print("Volume bola = ", volume)
print("-----------")


print("nomor 2")
lingkaran2 = BendaBulatDua(14)
print("jari jari lingkaran 2 : ", lingkaran2.getRadius())
print("luas lingkaran 2 : ", lingkaran2.luasLingkaran())
print("volume lingkaran 2 :  ", lingkaran2.volumeBola())
lingkaran2.setRadius()
print("luas lingkaran 2 : ", lingkaran2.luasLingkaran())
print("volume lingkaran 2 :  ", lingkaran2.volumeBola())
print("-----------")


print("nomor 3")
luas = bidangSegiEmpat.luasBujurSangkar(14)
print("luas segi empat = ", luas)
luasP = bidangSegiEmpat.luasPersegiPanjang(14, 2)
print("Volume persegi panjang = ", luasP)
print("-----------")

print("nomor 4")
persegiPanjang = bidangSegiEmpatDua(14, 2)
print("panjang persegi panjang : ", persegiPanjang.getPanjang())
print("lebar persegi panjang : ", persegiPanjang.getLebar())
persegiPanjang.setPanjang()
persegiPanjang.setLebar()
print("luas persegi panjang : ", persegiPanjang.luasPersegiPanjang())
