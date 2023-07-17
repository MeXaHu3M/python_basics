"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.

Пример:
Ведите целое положительное число: 123456789
Самая большая цифра в числе: 9
"""

num = int(input("Введите натуральное число\n"))
highest = 0
while num // 10:
    if highest < num % 10:
        highest = num % 10
    num = num // 10
print(highest)
