# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['яблоко', 'банан', 'киви', 'арбуз']
for index, fruit in en(fruits, start = 1):
    index = str(index)
    print((index+'.'), '{:>4}'.format(fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

spisok1 = list(map(int,input('Введите числа первого списка через пробел, затем нажмите Enter ').split()))
spisok2 = list(map(int,input('Введите числа второго списка через пробел, затем нажмите Enter ').split()))
for i in spisok2:
	if i in spisok1:
		spisok1.remove(i)
print("Второй список: ", spisok1)
print("Первый список: ", spisok2)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

sp1 = list(map(int,input('Введите числа первого списка через пробел, затем нажмите Enter ').split()))
sp2 = []
for i in sp1:
	if i % 2 == 0:
		i /= 4
		sp2.append(round(i))
	else:
		i *=2
		sp2.append(i)
print("Второй список: ", sp2)
