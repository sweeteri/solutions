# кол-во пар, произвеление кратно 65

with open('27B.txt') as f:
    n = int(f.readline())
    k65, k5, k13, k = 0, 0, 0, 0
    for _ in range(n):
        x = int(f.readline())
        if x % 13 == 0 and x % 5 == 0:
            k65 += 1
        elif x % 5 == 0:
            k5 += 1
        elif x % 13 == 0:
            k13 += 1
        else:
            k += 1

print(k65*k + k65*k5 + k65*k13 + k5 * k13 + k65*(k65-1)//2)
