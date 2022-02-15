import math
import random
print("Введите целое число: ")
x = int(input())
print("Квадрат этого числа:  ", x**2)
print("Факториал этого числа:  ", math.factorial(x))
i = 0
A = []
print("Массив размера введенного числа с рандомным наполнением:")
for i in range(x):
    A.append(random.randint(0, 1000))
    print(A[i])

