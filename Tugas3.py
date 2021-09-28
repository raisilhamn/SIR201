import math


class BendaBulat ():
    __rad = 0
    __luasLingkaran = float(0)
    __volimeLingkaran = float(0)
    __kelilingLingkaran = float(0)

    def setRadius(self, radius):
        self.__rad = radius

    def getLuasLingkaran(self):
        self.__luasLingkaran = ((math.pow(self.__rad, 2))*math.pi)
        return self.__luasLingkaran

    def getVolumeLingkaran(self):
        self.__volimeLingkaran = ((math.pow(self.__rad, 3))*(4/3)*math.pi)
        return self.__volimeLingkaran

    def getKelilingLingkaran(self):
        self.__kelilingLingkaran = (math.pi*2*self.__rad)
        return self.__kelilingLingkaran


print("============= SOAL 1 =============")
lingkaran = BendaBulat()
radius = 14
lingkaran.setRadius(radius)
print("Luas lingkaran : ", lingkaran.getLuasLingkaran())
print("Luas volume : ", lingkaran.getVolumeLingkaran())
print("Luas keliling : ", lingkaran.getKelilingLingkaran())


class BidangSegi4 ():
    __panjang = 0
    __lebar = 0
    __hasil = 0

    def setPanjang(self, x):
        self.__panjang = x

    def setLebar(self, x):
        self.__lebar = x

    def getPanjang(self):
        return self.__panjang

    def getLebar(self):
        return self.__lebar

    def luasBujurSangkar(self):
        self.__hasil = self.__panjang*self.__panjang
        print("luas Persegi = ", self.__hasil)

    def luasPersegiPanjang(self):
        self.__hasil = self.__panjang*self.__lebar
        print("luas PersegiPanjang = ", self.__hasil)

    def KelilingBujurSangkar(self):
        self.__hasil = (self.__panjang)*4
        print("Keliling Persegi = ", self.__hasil)

    def KelilingPersegiPanjang(self):
        self.__hasil = (self.__panjang+self.__lebar)*2
        print("Keliling Persegipanjang = ", self.__hasil)


print("============= SOAL 2 =============")
sisi = 12
persegi = BidangSegi4()
persegi.setPanjang(sisi)
persegi.luasBujurSangkar()
persegi.KelilingBujurSangkar()
print("Panjang persegi : ", persegi.getPanjang())

print("---")
panjang = 12
lebar = 14
persegiPanjang = BidangSegi4()
persegiPanjang.setPanjang(panjang)
persegiPanjang.setLebar(lebar)
persegiPanjang.luasPersegiPanjang()
persegiPanjang.KelilingPersegiPanjang()
print("panjang persegipanjang : ", persegiPanjang.getPanjang())
print("lebar persegipanjang : ", persegiPanjang.getLebar())
print("==================================")
