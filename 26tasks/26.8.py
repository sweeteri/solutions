'''
Иван коллекционирует старые марки. Он собирает все марки, которые ему удается найти,
которые были выпущены в его стране за определённые годы. Иван знает, что в эти годы
каждый год выпускалось 8 различных типов марок Иван решил проверить свою коллекцию и понять,
скольких видов марок ему не хватает и для какого самого позднего года ему не хватает наибольшего количества марок
до полного набора.
'''

with open('26.txt') as f:
    n = int(f.readline())
    d = {}

    for i in f:
        k, v = map(int, f.readline().split())
        d.setdefault(k, set()).add(v)

    marks_amount, year, max_marks_amount = 0, 0, 0
    for i in sorted(d, reverse=True):
        marks_amount += (8 - len(d[i]))
        if (8 - len(d[i])) > max_marks_amount:
            max_marks_amount = (8 - len(d[i]))
            year = i

print(marks_amount, year)
