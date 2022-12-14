'''
Для перевозки партии грузов различной массы выкупают место у компании перевозчиков.
 Компания перевозчик не может принять на борт больше 5 тонн груза.
 Известно, что отдельный груз нельзя разделить для перевозки,
 то есть один груз должен доставляться одним рейсом на одном грузовом судне.
 Так же преследуют тактику - перевезти рейсом грузы как можно большей массы.
 В ответе запишите два числа - минимальное количество рейсов и суммарную массу грузов,
 которые будут перевезены последним рейсом
 '''

with open('26.txt') as f:
    n, S = map(int, f.readline().split())
    lst = sorted([int(x) for x in f], reverse=True)
    trips = []
    s = 0
    while len(lst) != 0:
        for i in range(len(lst)):
            if s + lst[i] <= S:
                s += lst[i]
                lst[i] = 0
        lst = [x for x in lst if x != 0]
        trips.append(s)
        s = 0
print(len(trips), trips[-1])
