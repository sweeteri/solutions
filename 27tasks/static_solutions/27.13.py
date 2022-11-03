# минимальная сумма тройки кратная 11
with open('27B.txt') as f:
    n = int(f.readline())
    k = [[] for _ in range(11)]
    for _ in range(n):
        x = int(f.readline())
        k[x % 11].append(x)
a = []
for i in range(len(k)):
    k[i].sort()
    a += k[i][:3]

ans = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            if (a[i] + a[j] + a[k]) % 11 == 0:
                ans.append(a[i] + a[j] + a[k])
print(min(ans))
