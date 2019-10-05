#Вариант 4

# В качестве практической работы попробуйте самостоятельно перегрузить оператор сложения.
# Для его перегрузки используется метод __add__().
# Он вызывается, когда объекты класса, имеющего данный метод, фигурируют в операции сложения, причем с левой стороны.
# Это значит, что в выражении a + b у объекта должен быть метод __add__().
# Объект b может быть чем угодно, но чаще всего он бывает объектом того же класса.
# Объект b будет автоматически передаваться в метод __add__() в качестве второго аргумента (первый – self).
# Отметим, в Python также есть правосторонний метод перегрузки сложения - __radd__().
# Согласно полиморфизму ООП, возвращать метод __add__() может что угодно.
# Может вообще ничего не возвращать, а "молча" вносить изменения в какие-то уже существующие объекты.
# Допустим, в вашей программе метод перегрузки сложения будет возвращать новый объект того же класса.


class Add:
    def __init__(self, argument):
        self.argument = argument

    def __add__(self, second):
        if type(second) is int or type(second) is float:
            return Add(second + self.argument)
        elif type(second) is str:
            return Add(second + str(self.argument))
        elif type(second) is list:
            return Add(second + list(self.argument))
        else:
            return Add(second.argument + self.argument)

    def show(self):
        print(self.argument)


a = Add(12)
b = Add(24)
c = Add('r')
d = Add('l')
e = Add([4, 8, 1])
f = Add([1, 1])
g = a + 5
h = a + b
i = a + 1.3
j = a + 's'
k = c + 'g'
l = c + d
m = e + f
n = e + [1, 1, 1]
print(g)
g.show()
print(h)
h.show()
print(i)
i.show()
print(j)
j.show()
print(k)
k.show()
print(l)
l.show()
print(m)
m.show()
print(n)
n.show()