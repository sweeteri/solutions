# макс сумма 4ки чисел, произведение кратно 12
with open('27B.txt') as f:
    n = int(f.readline())
    k, k3, k4, k6, k12 = [], [], [], [], []
    for _ in range(n):
        x = int(f.readline())
        if (x % 3 == 0 and x % 4 == 0) or (x % 2 == 0 and x % 6 == 0):
            k12.append(x)
        elif x % 3 == 0:
            k3.append(x)
        elif x % 4 == 0:
            k4.append(x)
        elif x % 6 == 0:
            k6.append(x)
        else: k.append(x)
a = []
k.sort()
k3.sort()
k4.sort()
k6.sort()
k12.sort()
a += k[-4:]
a += k3[-4:]
a += k6[-4:]
a += k12[-4:]
a += k4[-4:]
ans = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
            for m in range(k+1, len(a)):
                if (a[i] * a[j] * a[k] * a[m]) % 12 == 0:
                    ans.append(a[i] + a[j] + a[k] + a[m])
print(max(ans))
