# колво пар сумма делится на 80, хотя бы один элемент из пары больше 50000
with open('27A.txt') as f:
    n = int(f.readline())
    k80 = [0] * 80
    b50000 = [0] * 80
    for _ in range(n):
        x = int(f.readline())
        if x > 50000:
            b50000[x % 80] += 1
        else:
            k80[x % 80] += 1

s = b50000[0]*(b50000[0]-1)//2 + b50000[40]*(b50000[40]-1)//2 + k80[40]*b50000[40] + k80[0]*b50000[0]

for i in range(1, 40):
    s += b50000[i]*b50000[80-i]
    s += k80[i]*b50000[80-i]
    s += b50000[i]*k80[80-i]

print(s)
