# самая редкая цифра, ее кол-во во всех числах набора
with open('27B.txt') as f:
    n = int(f.readline())
    a = [0] * 10
    for _ in range(n):
        x = int(f.readline())
        while x > 0:
            a[x % 10] += 1
            x //= 10
print(min(a))
