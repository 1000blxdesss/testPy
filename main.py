# from matplotlib import pyplot as plt
# Числа_фибо = []
# x=[]

"""
Функция принимает n и возвращает число Фибоначчи по индексу n
n = 5 -> 5
"""


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)


"""
Функция принимает список чисел 
и возвращает отсорт-ю версию
[1,2,3] -> [1,2,3]
[1,3,2] -> [1,2,3]
"""


def sort(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


"""
Функция принимает два числа
и возвращает результат операции между ними
(2,5)['*'] -> 10
"""


def math_oper(a, b):
    return {'*': a * b, '-': a - b, '+': a + b, '/': a / b}


def math_95945439(a, b, op):
    return {'*': a * b, '-': a - b, '+': a + b, '/': a / b}.get(op)


# if __name__ == '__main__':
#     for i in range(1, 11):
#         Числа_фибо.append(fibo(i))
#         x.append(i)
#     y = Числа_фибо
# plt.plot(x, y, color='green', marker='o', markersize=7)
# plt.xlabel('Номер Фибоначчи')
# plt.ylabel('Величина числа Фибоначчи')
# plt.show()
# print(Числа_фибо)
