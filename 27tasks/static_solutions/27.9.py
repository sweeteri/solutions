# колво пар сумма элементов равна 2000

with open('27B.txt') as f:
    n = int(f.readline())
    a = [0]*2000
    for _ in range(n):
        x = int(f.readline())
        if x < 2000:
            a[x] += 1

s = a[1000]*(a[1000]-1)//2
for i in range(1, 1000):
    s += a[i] * a[2000-i]

print(s)
