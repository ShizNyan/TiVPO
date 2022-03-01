#Научный калькулятор(решение уравнений, матричные операции, интегрирование и т. д.).
import math


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

    def test_matrix_add(self, c):
        print("testing matrix_add")
        mx = [[1, 1],
              [1, 1]]
        my = [[1, 1],
              [1, 1]]
        mres = [[2, 2],
                [2, 2]]
        res = c.matrix_add(mx, my, 2)
        if res == mres:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_matrix_sub(self, c):
        print("testing matrix_sub")
        mx = [[1, 1],
              [1, 1]]
        my = [[1, 1],
              [1, 1]]
        mres = [[0, 0],
                [0, 0]]
        res = c.matrix_sub(mx, my, 2)
        if res == mres:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_matrix_mul(self, c):
        print("testing matrix_mul")
        mx = [[1, 1],
              [1, 1]]
        my = [[2, 3],
              [2, 3]]
        mres = [[4, 6],
                [4, 6]]
        res = c.matrix_mul(mx, my, 2)
        if res == mres:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_matrix_transpose(self, c):
        print("testing matrix_transpose")
        mx = [[1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4]]
        mres = [[1, 1, 1, 1],
                [2, 2, 2, 2],
                [3, 3, 3, 3],
                [4, 4, 4, 4]]
        res = c.matrix_transpose(mx, 4)
        if res == mres:
            print("Тест пройден")
        else:
            print("Тест не пройден")

    def test_integrate(self, c):
        print("testing integrate")
        tres = 0.4221669591570937
        tres_r = -0.0003028591589098281
        res, res_r = c.integrate(c, 0, 1, 5)
        if res == tres and tres_r == res_r:
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

    def matrix_add(self, x, y, size):
        for i in range(size):
            for j in range(size):
                x[i][j] += y[i][j]
        return x

    def matrix_sub(self, x, y, size):
        for i in range(size):
            for j in range(size):
                x[i][j] -= y[i][j]
        return x

    def matrix_mul(self, x, y, size):
        res = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        t =0
        
        for i in range(size):
            for j in range(size):
                t += x[i][j]*y[j][i]
            res[i][j] = t
            t = 0
        return res

    def matrix_transpose(self, x, size):
        res = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        for i in range(size):
            for j in range(size):
                res[j][i] = x[i][j]
        return res

    def f(self, x): #функция интеграла
        return 1 / (1 + math.exp(x))

    def f_2(self, x):
        return (-1 + (2 * (math.exp(x) / (math.exp(x) + 1)))) * math.exp(x) / (pow((1 + math.exp(x)), 2))

    def integrate(self, c, a, b, k):

        x = [i for i in range(k)]
        k2 = k + 1

        I = 0 #решение интеграла
        I1 = 0 #первая часть интеграла
        I2 = 0 #вторая часть интеграла
        R = 0 #остаточный член
        h = 0 #шаг интегрирования
        max = 0 #максимальное значение второй производной функции на интервале
        h = (b - a) / k

        for i in range(k2-1):
            x[i] = c.f(h * i)

        I1 = (b - a) / k
        I2 = (x[0] + x[k-1]) / 2

        for i in range(k-1):
            I2 += x[i]
        

        max = c.f_2(b)

        R = (-(b - a) / 12) * pow(h, 2) * max

        I = I1 * I2
    
        return I, R
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
    print("5 - Сложение матриц (4х4)")
    print("6 - Вычитание матриц (4х4)")
    print("7 - Умножение матриц (4х4)")
    print("8 - Транспонирование матрицы (4х4)")
    print("9 - Интегрирование по частям")
    print("10 - Закончить работу")
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

    elif m == 5:
        matrix_x = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        matrix_y = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

        size = 4
        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (size):
            print(matrix_x[i])
        print()

        print("Введите матрицу y")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_y[i][j] = k
        print()
        print("Матрица y:")
        for i in range (size):
            print(matrix_y[i])

        print()

        res = c.matrix_add(matrix_x, matrix_y, size)
        print("Результат сложения матриц:")
        for i in range (size):
            print(res[i])
        t.test_matrix_add(c)

    elif m == 6:
        matrix_x = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        matrix_y = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

        size = 4
        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (size):
            print(matrix_x[i])
        print()

        print("Введите матрицу y")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_y[i][j] = k
        print()
        print("Матрица y:")
        for i in range (size):
            print(matrix_y[i])
        print()

        res = c.matrix_sub(matrix_x, matrix_y, size)
        print("Результат вычитания матриц:")
        for i in range (size):
            print(res[i])
        t.test_matrix_sub(c)

    elif m == 7:
        matrix_x = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
        matrix_y = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

        size = 4
        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (size):
            print(matrix_x[i])
        print()

        print("Введите матрицу y")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_y[i][j] = k
        print()
        print("Матрица y:")
        for i in range (size):
            print(matrix_y[i])
        print()

        res = c.matrix_mul(matrix_x, matrix_y, size)
        print("Результат умножения матриц:")
        for i in range (size):
            print(res[i])
        t.test_matrix_mul(c)

    elif m == 8:
        matrix_x = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

        size = 4
        print("Введите матрицу x")
        for i in range (size):
            print("Введите строку "+str(i+1))
            for j in range (size):
                k = int(input())
                matrix_x[i][j] = k
        print()
        print("Матрица x:")
        for i in range (size):
            print(matrix_x[i])
        print()

        res = c.matrix_transpose(matrix_x, size)
        print("Результат транспонирования матрицы:")
        for i in range (size):
            print(res[i])
        t.test_matrix_transpose(c)

    elif m == 9:
        a = 0 #пределы интегрирования
        b = 1
        print("Введите количество интервалов разбиения")
        k = int(input())
        res, res_r = c.integrate(c, a, b, k)
        print("Результат интегрирования по частям:")
        print(res,"+-",res_r)
        t.test_integrate(c)

    elif m == 10:
        print("Закончить работу")
        run = False

    
