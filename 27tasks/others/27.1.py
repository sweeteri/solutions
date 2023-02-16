"""
Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так,
чтобы сумма всех выбранных чисел не делилась на 3 и при этом была максимально возможной.
"""
with open('27-B.txt') as f:
    f.readline()
    s = 0
    min_delta = 10001
    for i in f:
        num1, num2 = map(int, i.split())
        s += max(num1, num2)
        if abs(num1 - num2) % 3 != 0:
            min_delta = min(min_delta, abs(num1 - num2))
print(s if s % 3 != 0 else s - min_delta)
