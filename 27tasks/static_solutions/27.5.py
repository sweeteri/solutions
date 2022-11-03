# кол-во троек, где все числа кратны 19
with open('27B.txt') as f:
    n = int(f.readline())
    k19 = 0
    for _ in range(n):
        if int(f.readline()) % 19 == 0:
            k19 += 1
print(k19*(k19-1)*(k19-2)//6)
