# координаты
# найти наибольшую площадь треугольника, одна из сторон которого лежит на оси ох
with open('27B.txt') as f:
    n = int(f.readline())
    x_min, x_max, y_max = 1000000000, -10000000000000, 0
    for _ in range(n):
        x, y = map(int, f.readline().split())
        if y == 0 and x < x_min:
            x_min = x
        if y == 0 and x > x_max:
            x_max = x
        if abs(y) > abs(y_max):
            y_max = abs(y)

print(0.5 * (x_max - x_min) * y_max)
