#  колво пар разность кратна 69
with open('27B.txt') as f:
    n = int(f.readline())
    k = [0] * 69
    for _ in range(n):
        x = int(f.readline())
        k[x % 69] += 1
s = 0
for i in range(69):
    s += k[i] * (k[i]-1)//2

print(s)