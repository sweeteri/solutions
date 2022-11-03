# кол-во пар чисел, у которых сумма четна
with open('27B.txt') as file:
    n = int(file.readline())
    k1, k0 = 0, 0
    for _ in range(n):
        if int(file.readline()) % 2:
            k1 += 1
        else:
            k0 += 1
print(k1*(k1-1)//2+k0*(k0-1)//2)
