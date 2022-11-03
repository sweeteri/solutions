# максимальная разность пары элементов, разность которых делится на 80
with open('27B.txt') as f:
    n = int(f.readline())
    a = [[] for _ in range(80)]
    for _ in range(n):
        x = int(f.readline())
        a[x % 80].append(x)
a1 = []
for i in range(len(a)):
    if len(a[i]) != 0:
        a1.append(max(a[i])-min(a[i]))
print(max(a1))
