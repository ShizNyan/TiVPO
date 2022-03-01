#Научный калькулятор(решение уравнений, матричные операции, интегрирование и т. д.).


print("Hello there")

class Test():
    
    def test_add(self, c):
        print("testing add")
        if c.add(2, 2) == 4:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_sub(self, c):
        print("testing sub")
        if c.sub(2, 1) == 1:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_mul(self, c):
        print("testing mul")
        if c.mul(1, 1) == 1:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_div(self, c):
        print("testing div")
        if c.div(2, 1) == 2:
            print("Тест пройден")
        else:
            print("Тест не пройден")


class Calculator():

    def add(self, x, y):
        return x+y

    def sub(self, x, y):
        return x-y

    def mul(self, x, y):
        return x*y

    def div(self, x, y):
        if y!=0:
            return x/y
        else:
            return "N/A"

    def matrix_add(self, x, y):
        
        print("+")

    def matrix_sub(self, x, y):
        print("-")

    def matrix_mul(self, x, y):
        print("*")

    def matrix_transpose(self, x, y):
        print("T")

    def matrix_reverse(self, x, y):
        print("R")

    def integrate(self, x, y):
        print("Integral")


print("Program starts here")

run = True
c = Calculator()
t = Test()

while (run):
    
    print()
    print("Введите х - число от 1 до 4, где:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")
    print("5 - Решение уравнения??")
    print("6 - Сложение матриц")
    print("7 - Вычитание матриц")
    print("8 - Умножение матриц")
    print("9 - Транспонирование матриц")
    print("10 - Нахождение обратно матрицы")
    print("11 - Интегрирование")
    print("12 - Закончить работу")
    m = int(input())

    if m == 1:
        print("Введите x и y")
        x = int(input())
        y = int(input())
        res = c.add(x,y)
        print("Результат сложения:")
        print(res)
        t.test_add(c)

    elif m == 2:
        print("Введите x и y")
        x = int(input())
        y = int(input())
        res = c.sub(x,y)
        print("Результат вычитания:")
        print(res)
        t.test_sub(c)

    elif m == 3:
        print("Введите x и y")
        x = int(input())
        y = int(input())
        res = c.mul(x,y)
        print("Результат умножения:")
        print(res)
        t.test_mul(c)

    elif m == 4:
        print("Введите x и y")
        x = int(input())
        y = int(input())
        res = c.div(x,y)
        print("Результат деления:")
        if res != "N/A":
            print(res)
        else:
            print("N/A")
        t.test_div(c)

    elif m == 6:
        matrix_x = []
        matrix_y = []

        print("Введите размерность матриц")
        size = int(input())
        print()
        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (4):
            print(matrix_x[i])
        print()

        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (4):
            print(matrix_x[i])

        print()

        res = c.matrix_add(matrix_x, matrix_y)
        print("Результат деления:")
        if res != "N/A":
            print(res)
        else:
            print("N/A")
        t.test_div(c)

    elif m == 12:
        print("Закончить работу")
        run = False

    
