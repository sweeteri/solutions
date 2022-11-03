# минимальное произведение кратное 31

with open('27A.txt') as f:
    n = int(f.readline())
    k31, k = [], []
    for _ in range(n):
        x = int(f.readline())
        if x % 31 == 0:
            k31.append(x)
        else: k.append(x)
k31.sort()
print(min(k31[0]*k31[0], k31[0]*min(k)))
