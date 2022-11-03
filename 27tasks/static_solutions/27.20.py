# координаты
# найти кол-во тругольников, включая вырожденнные,
# одна вершина лежит на оси ох, другая на оси оу,
# третья не лежит ни на одной оси
with open('27A.txt') as f:
    y0, x0, m = 0, 0, 0
    n = int(f.readline())
    for _ in range(n):
        x, y = map(int, f.readline().split())
        if x == 0:
            x0 += 1
        elif y == 0:
            y0 += 1
        else:
            m += 1
print(x0*y0*m)
