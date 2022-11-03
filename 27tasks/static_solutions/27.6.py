#  колво пар сумма кратна 131
with open('27B.txt') as f:
    n = int(f.readline())
    k = [0] * 131
    for _ in range(n):
        x = int(f.readline())
        k[x % 131] += 1
s = k[0]*(k[0]-1)//2
for i in range(1, 66):
    s += k[i] * k[131-i]

print(s)
