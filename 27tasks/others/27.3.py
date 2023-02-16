"""
Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так,
чтобы сумма всех выбранных чисел не делилась на 5 и при этом была минимально возможной.
"""
with open('27-B.txt') as f:
    f.readline()
    s = 0
    min_delta = 10001
    for i in f:
        num1, num2 = map(int, i.split())
        s += min(num1, num2)
        if abs(num1 - num2) % 10 not in (0, 5):
            min_delta = min(min_delta, abs(num1 - num2))
print(s if s % 5 != 0 else s + min_delta)
