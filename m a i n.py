# Создайте новую функцию def test... с произвольным числом параметров разного типа, функция должна распечатывать эти параметры внутри своего тела
# Создайте рекурсивную функцию, которая будет считать факториал от числа n, n - передается в параметре
# В ответ прикрепите получившийся файл main.py

def test(*param):
    print(*param)  # выводит аргументы из кортежа
    print(param)  # выводит кортеж


test(1, 2, '3', "4", 1.3, True, False)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))
