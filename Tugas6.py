# 1
import pprint  # To display "3d array" in a recognizable format
import random
import pprint  # To display "3d array" in a recognizable format
import numpy as np


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


# 2 array 2 dimensi sama 

class Matriks:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.data = []

    def Matriks2DSama(self):
        for i in range(self.row):
            arrCol = []
            for j in range(self.col):
                temp = int(input(F'masukkan nilai indeks ke {i} {j} =  '))
                arrCol.append(temp)
            self.data.append(arrCol)
        return self

    def tampilArray(self):
        for n in self.data:
            print(n)

    def Penjumlahan2D(self, other):
        if self.col == other.col and self.row == other.row:
            result = np.add(self.data, other.data)
            for n in result:
                print(n)
        else:
            print('Tidak bisa menjumlah matriks, dimensi beda')

    def Pengurangan2D(self, other):
        if self.col == other.col and self.row == other.row:
            result = np.subtract(self.data, other.data)
            for n in result:
                print(n)
        else:
            print('Tidak bisa menjumlah matriks, dimensi beda')


class Array2DimBedaElemen:
    def __init__(self, row):
        self.row = row
        self.data = []

    def Matriks(self):
        for i in range(self.row):
            arrCol = []
            a = int(
                input(F'Masukan berapa banyak kolom untuk baris ke {i} = '))
            for j in range(a):
                temp = int(
                    input(F'masukkan nilai indeks ke {i} {j} =  '))
                arrCol.append(temp)
            self.data.append(arrCol)
        row_lengths = []
        for n in self.data:
            row_lengths.append(len(n))
        max_length = max(row_lengths)
        for n in self.data:
            while len(n) < max_length:
                n.append(None)
        return self

    def tampilArray(self):
        for n in self.data:
            print(n)


# Array3DimSama


class Array3DimSama:
    def __init__(self, baris, kolom, tinggi):
        self.data = [[[0 for _ in range(baris)]
                      for _ in range(kolom)] for _ in range(tinggi)]
        self.baris = baris
        self.kolom = kolom
        self.tinggi = tinggi

    def Matriks(self):
        for baris in range(self.baris):
            for kolom in range(self.kolom):
                for tinggi in range(self.tinggi):
                    # print('Masukkan baris kolom tinggi : ', baris, kolom, tinggi)
                    # self.data[baris][kolom][tinggi] = int(input())
                    self.data[baris][kolom][tinggi] = int(random.randint(0, 9))

    def tampilArray(self):
        pprint.pprint(self.data)

    def tambahArray(self, other):
        if self.baris != other.baris or self.kolom != other.kolom or self.tinggi != other.tinggi:
            print('tidak bisa menambahkan array, bentuk berbeda')
        else:
            for baris in range(self.baris):
                for kolom in range(self.kolom):
                    for tinggi in range(self.tinggi):
                        self.data[baris][kolom][tinggi] += other.data[baris][kolom][tinggi]

    def kurangArray(self, other):
        if self.baris != other.baris or self.kolom != other.kolom or self.tinggi != other.tinggi:
            print('tidak bisa menambahkan array, bentuk berbeda')
        else:
            for baris in range(self.baris):
                for kolom in range(self.kolom):
                    for tinggi in range(self.tinggi):
                        self.data[baris][kolom][tinggi] -= other.data[baris][kolom][tinggi]


print('=========================== Nomor 1 (vektor) =========================== ')
v1 = Vektor(3, 2, 1, 0)
v2 = Vektor(1, 3, 5, 7)
print(f"Vektor 1 = {v1.tampilVektor()}")
print(f"Vektor 2 = {v2.tampilVektor()}")
print(f"Jumlah Vektor 1 dan 2 = {v1.jumlah2Vektor(v2)}")
print(f"Jumlah Vektor 1 dan Vektor 1 = {v1.jumlah2Vektor()}")
print(f"Selisih Vektor 1 dan Vektor 2 = {v1.selisih2Vektor(v2)}")
print(f"Selisih Vektor 1 dan Vektor 1 = {v1.selisih2Vektor()}")

print('=========================== Nomor 2 (array 2 dimensi) =========================== ')
print('======= masukan tiap elemen array 1 ========= ')
test1 = Matriks(2, 2)
test1.Matriks2DSama()
test1.tampilArray()
print('======= masukan tiap elemen array 2 ========= ')
test2 = Matriks(2, 2)
test2.Matriks2DSama()
test2.tampilArray()

print('======= array 1 ========= ')
test1.tampilArray()
print('======= array 2 ========= ')
test2.tampilArray()

print("======= Penjumlahan 2 matriks 2D ======= ")
test2.Penjumlahan2D(test1)

print("======= Pengurangan 2 matriks 2D ======= ")
test1.Penjumlahan2D(test2)

print('=========================== Nomor 3 (array 2D baris tidak sama) =========================== ')
barisArray = int(input(F'Masukan jumlah baris array : '))
test4 = Array2DimBedaElemen(barisArray)
test4.Matriks()
test4.tampilArray()

test5 = Array2DimBedaElemen(barisArray)
test5.Matriks()
test5.tampilArray()


print('======= array 1 ========= ')
test4.tampilArray()
print('======= array 2 ========= ')
test5.tampilArray()



print('=========================== Nomor 3 (Array 3 dimensi) =========================== ')
print('======= masukan tiap elemen array 1 ========= ')
array3d = Array3DimSama(3, 3, 3)
array3d.Matriks()

print('======= masukan tiap elemen array 2 ========= ')
array3d2 = Array3DimSama(3, 3, 3)
array3d2.Matriks()

print('======= array 1 ========= ')
array3d.tampilArray()
print('======= array 2 ========= ')
array3d2.tampilArray()

array3d.tambahArray(array3d2)

print('======= hasil tambah array ========= ')
array3d.tampilArray()

array3d2.kurangArray(array3d)
print('======= hasil kurang array ========= ')
array3d2.tampilArray()

