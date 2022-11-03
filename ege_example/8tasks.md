### Размещения
```python
from itertools import product


s = 'HELLO'

# возвращает итератор из кортежей комбинаций символов
for i in product(s, repeat=4): #  параметр repeat отвечает за количество символов в комбинации
    word = ''.join(i) # склеиваем кортеж в строку
    print(word)

# без itertools
for a in s:
    for b in s:
        for c in s:
            for d in s:
                word = a + b + c + d
                print(word)
                
# можно задавать на каком месте стоят определенные буквы
# первая: ADB, вторая: ASD, третья: LKJ
for i in product('ADB', 'ASD', 'LKJ'): 
    word = ''.join(i) 
    print(word)
```
### Перестановки
```python
from itertools import permutations
# возвращает итератор из кортежей комбинаций символов
# ВАЖНО!!! Если в строке есть одинаковые символы, то они считаются за разные,
# поэтому для получения точного количества перестановок надо получить множество
```

