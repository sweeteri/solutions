# минимальное произведение пары чисел, кратное 31
with open('27B.txt') as f:
    n = int(f.readline())
    min31, minn = 10 ** 5 + 1, 10 ** 5 + 1
    arr = []
    for _ in range(n):
        x = int(f.readline())
        if x % 31 == 0:
            min31 = min(min31, x)
        else:
            minn = min(minn, x)

print(min(min31 * min31, minn * min31))
