# Задание 1 "Список четных эелементов"
print("\n--- Задание 1 ---")
n1 = int(input("Введите количесво елементов списка:"))
L1 = []

print("Введите элементы списка: ")
for i in range(n1):
    L1.append(int(input()))

print(L1)
l1 = []
for i in range(n1):
    if L1[i] % 2 == 0:
        l1.append(L1[i])

print("Список четных элементов:\n", l1)


# Задание 2 "Список эелементов с четными индексами"
print("\n--- Задание 2 ---")
n2 = int(input("Введите количесво елементов списка:"))
L2 = []

print("Введите элементы списка: ")
for i in range(n2):
    L2.append(int(input()))

print(L2)
l2 = []
for i in range(n2):
    if i % 2 == 0:
        l2.append(L2[i])

print("Список элементов с четными индексами:\n", l2)


# Задание 3 "Список положительных эелементов"
print("\n--- Задание 3 ---")
n3 = int(input("Введите количесво елементов списка:"))
L3 = []

print("Введите элементы списка: ")
for i in range(n3):
    L3.append(int(input()))

print(L3)
l3 = []
for i in range(n3):
    if L3[i] >= 0:
        l3.append(L3[i])

print("Список элементов с четными индексами:\n", l3)


# Задание 4 "Список  множеств остатот от которыхпри делении на m дает одинаковй остаток "
print("\n--- Задание 4 ---")

L4 = [1, 3, 4, 7, 9]
m = 3
l4 = []
M = []
K = []
for i in range(len(L4)):
    l4.clear()
    k = L4[i] % m
    while k not in K:
        K.append(k)
        for j in range(len(L4)):
            if (L4[j] % m) == k:
                l4.append(L4[j])

        M.append(set(l4))
print(M)


# Задание 5 "Список  сумм ключей и их значений, если ключи b значения числа - числа "
print("\n--- Задание 5 ---")
D = {1: 2, 'a': 3, -1: 1, 3: 'a'}

l5 = []
for i in D:
    if type(D[i]) == int and type(i) == int:
        l5.append(i + D[i])

print(l5)


# Задание 7 "Словарь ключами которого служат элементы списка L c четными индексами,  а значениями - нечетные "
print("\n--- Задание 7 ---")
L = ['a', 1, -2, 1.2]
S = {}

for i in range(len(L)):
    if i % 2 == 0:
        S[L[i]] = L[i+1]

print(S)


