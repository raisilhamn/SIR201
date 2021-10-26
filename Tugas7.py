# 1
import math


class B:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def showA(self):
        print(self.__a)

    def showB(self):
        print(self.__b)


class D(B):
    def mul(self):
        c = self.getB()*self.getA()
        return c

    def dev(self):
        d = self.getB()/self.getA()
        return d

    def display(self, w, x, y, z):
        print(f"A = {self.getA()} ")
        print(f"B = {self.getB()} ")
        print(f"C = {self.mul()} ")
        print(f"D = {self.dev()} ")


print('======= Nomor 1 =======')
soal1 = D(10, 13)
print(f"A = {soal1.getA()}")
print(f"B = {soal1.getB()}")
print(f"C = {soal1.mul()}")
print(f"D = {soal1.dev()}")

# 2


class Student:
    def __init__(self, a):
        self.__rollNumber = a

    def putNumber(self):
        return self.__rollNumber


class Test(Student):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.sub1 = b
        self.sub2 = c

    def putMarks(self):
        return self.sub1, self.sub2


class Result(Test):
    def display(self):
        total = self.sub2+self.sub1
        x, y = self.putMarks()
        print(f"Roll Number = {self.putNumber()} ")
        print(f"Sub 1 = {x} ")
        print(f"Sub 2 = {y} ")
        print(f"Total = {total} ")


print('======= Nomor 2 =======')
soal2 = Result(12, 4, 3)
soal2.display()

# 3


class Shape:
    def __init__(self, a):
        self.__name = a

    def getName(self):
        return self.__name

    def calculateArea(self):
        pass


class Circle(Shape):
    def __init__(self, a, r):
        super().__init__(a=a)
        self.radius = r

    def calculateArea(self):
        res = math.pow(self.radius, 2) * math.pi
        return res


class Square(Shape):
    def __init__(self, a, s):
        super().__init__(a=a)
        self.side = s

    def calculateArea(self):
        res = math.pow(self.side, 2)
        return res


print('======= Nomor 3 =======')
soal3 = Circle("Lingkaran", 10)
print(f"NAMA SHAPE = {soal3.getName()}")
print(f"Luas Lingkaran = {soal3.calculateArea()}")
test3 = Square("Persegi", 10)
print(f"NAMA SHAPE = {test3.getName()}")
print(f"Luas Persegi = {test3.calculateArea()}")
