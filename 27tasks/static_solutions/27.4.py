# кол-во пар произведение кратно 5, сумма нечетна

with open('27B.txt') as file:
    n = int(file.readline())
    k50, k51, nk50, nk51 = 0, 0, 0, 0
    for _ in range(n):
        x = int(file.readline())
        if x % 5 == 0:
            if x % 2:
                k51 += 1
            else:
                k50 += 1
        else:
            if x % 2:
                nk51 += 1
            else:
                nk50 += 1
print(nk50*k51 + nk51*k50 + k50*k51)
