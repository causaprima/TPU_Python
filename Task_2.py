import random
import xlwt

# Сортировка вставками
def sort_type(a):
    for i in range(len(a)):
        x = a[i]
        j = i
        while a[j-1] > x and j > 0:
            a[j] = a[j-1]
            j = j - 1
        a[j] = x
    return a


wb = xlwt.Workbook()
ws = wb.add_sheet('Сортировка')
numbers = [random.randint(0, 100) for i in range(100)]
i, j = 0, 0
for x in numbers:
    ws.write(i, j, x)
    i += 1
i, j = 0, 1
for y in sort_type(numbers):
    ws.write(i, j, y)
    i += 1
wb.save('first.xls')
