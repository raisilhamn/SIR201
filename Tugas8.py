import math


# menampilkan variabel yang dimiliki objek
def printVar(obj):
    res = []
    for i in range(len(obj)):
        if not obj[i].startswith("_"):
            res.append(obj[i])
    return res


class Vehicle:
    def start(self):
        print("Vehicle start code")

    def stop(self):
        print("Vehicle stop code")


class Car(Vehicle):
    __nbOfSeats = int

    def setnbOfSeats(self, num):
        self.__nbOfSeats = num

    def getNbOfSeats(self):
        return self.__nbOfSeats


car = Car()

print()
print("########### SOAL 1 ###########")
print("Objek car")
print(f"Variabel yang dapat diakses : {printVar(dir(car))}\n")

car.__class__ = Vehicle  # upcasting
vehicle_obj = car

print("Objek setelah upcasting")
print(f"Variabel yang dapat diakses : {printVar(dir(vehicle_obj))}\n")

vehicle_obj.__class__ = Car  # downcasting
car2 = vehicle_obj

print("Objek setelah downcasting")
print(f"Variabel yang dapat diakses : {printVar(dir(car2))}")


# 2
class Vehicle:
    def start(self):
        print("Vehicle start code")

    def stop(self):
        print("Vehicle stop code")


class Car(Vehicle):
    __nbOfSeats = int

    def setnbOfSeats(self, a):
        self.__nbOfSeats = a

    def start(self):
        print("Car start code")

    def getNbOfSeats(self):
        return self.__nbOfSeats


car = Car()

print()
print("########### SOAL 2 ###########")
print("Objek car = ")
print(f"Variabel yang dapat diakses : {printVar(dir(car))}\n")

car.__class__ = Vehicle
vehicle_obj = car
print("Objek Objek setelah upcasting ")
print(f"Variabel yang dapat diakses : {printVar(dir(vehicle_obj))}\n")

vehicle_obj.__class__ = Car  # downcasting
car2 = vehicle_obj

print("Objek setelah downcasting = ")
print(f"Variabel yang dapat diakses : {printVar(dir(car2))}")


# 3

class BendaBulat:
    def __init__(self, rad, color):
        self.__radius = rad
        self.__warna = color

    def getRadius(self):
        return self.__radius

    def getWarna(self):
        return self.__warna

    def display(self):
        print(self.getRadius())
        print(self.getWarna())


class Tabung(BendaBulat):
    def __init__(self, rad, color, tinggi):
        super().__init__(rad, color)
        self.__tinggi = tinggi

    def getTinggi(self):
        return self.__tinggi

    def display(self):
        print(self.getRadius)
        print(self.getWarna)
        print(self.getTinggi)

    def luaspermukaanTabung(self):
        if self.__radius is not None and self.__tinggi is not None:
            lp = (2 * math.pi * self.__radius * self.__tinggi) + \
                 (2 * math.pi * math.sqrt(self.__radius))
            return lp


tb1 = Tabung(3, "Hijau", 4)

print()
print("########### SOAL 3 ###########")

print("Objek tb1 = ")
print(f"Variabel yang dapat diakses : {printVar(dir(tb1))}\n")

tb1.__class__ = BendaBulat  # upcasting
bb1 = tb1

print("Objek setelah upcasting")
print(f"Variabel yang dapat diakses : {printVar(dir(bb1))}\n")

bb1.__class__ = Tabung  # downcasting
tb2 = bb1

print("Objek tb2 = ")
print(f"Variabel setelah downcasting : {printVar(dir(tb2))}")


class BendaPersegi:
    def __init__(self, panjang, lebar, warna="Hijau"):
        self.__panjang = panjang
        self.__lebar = lebar
        self.__warna = warna

    def getPanjang(self):
        return self.__panjang

    def getLebar(self):
        return self.__lebar

    def getWarna(self):
        return self.__warna

    def display(self):
        print(self.getPanjang())
        print(self.getLebar())
        print(self.getWarna())


class Balok(BendaPersegi):
    def __init__(self, panjang, lebar, warna, tinggi):
        super().__init__(panjang, lebar, warna=warna)
        self.__tinggi = tinggi

    def getTinggi(self):
        return self.__tinggi

    def display(self):
        print(self.getPanjang())
        print(self.getPanjang())
        print(self.getWarna())
        print(self.getTinggi())

    def volume(self):
        return self.getPanjang() * self.getPanjang() * self.getTinggi()


tb1 = Balok(3, 4, "Merah", 5)

print()
print("########### SOAL 4 ###########")

print("Objek tb1 = ")
print(f"Variabel yang dapat diakses : {printVar(dir(tb1))}\n")

tb1.__class__ = BendaBulat  # upcasting
bb1 = tb1

print("Objek setelah upcasting")
print(f"Variabel yang dapat diakses : {printVar(dir(bb1))}\n")

bb1.__class__ = Tabung  # downcasting
tb2 = bb1

print("Method tb2 = ")
print(f"Variabel setelah downcasting : {printVar(dir(tb2))}")
