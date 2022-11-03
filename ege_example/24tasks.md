# 24 задание
### Решение цепочек через кратность
Пример 
```
Текстовый файл состоит не более чем из 10^6 символов и
содержит только заглавные буквы латинского алфавита (ABC…Z).
Файл разбит на строки различной длины.
Определите максимальную длину цепочки символов,
состоящей из повторяющихся фрагментов XYZ.
Цепочка должна начинаться с символа X 
и заканчиваться символом Z.
Например, для строки SAZZXYZXYZXZQW 
длина цепочки равна 6: XYZ+XYZ.
```
```python
with open('file_name') as f:
    s = f.readline()
    current_max, max_max = 0, 0
    for i in range(len(s)):
        if (s[i] == 'X' and current_max % 3 == 0) or (
                s[i] == 'Y' and current_max % 3 == 1) or (
                s[i] == 'Z' and current_max % 3 == 2):
            current_max += 1
            max_max = max(max_max, current_max)
        elif s[i] == 'X':
            current_max = 1
        else:
            current_max = 0
    print(max_max)
```
### Количество подряд идущих пар
Пример
```
Найдите максимальное количество подряд идущих пар символов АС или АВ.
Искомая подстрока может включать только пары АВ,
только пары АС или содержать
одновременно как пары АС, так и пары АВ.
```
```python
with open('24.txt') as f:
    s = f.readline().strip()

i = 0
k = 0
k_max = 0
while i < len(s) - 1:
    if s[i] == 'A' and (s[i + 1] == 'B' or s[i + 1] == 'C'):
        k += 1
        i += 2
    else:
        k_max = max(k, k_max)
        k = 0
        i += 1
print(k_max)
```