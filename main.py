from datetime import datetime
import functions as f
import os

APP_DIR = os.path.dirname(os.path.realpath(__file__))

# print(f.get_current_timedate())
# print(f.write_file(name="test", data=time))


def xy():
    Primer = ("Пример-(x*y)/(g+z)")
    print(Primer)
    x = int(input("Чему равен x"))
    y = int(input("Чему равен y"))
    g = int(input("Чему равен g"))
    z = int(input("Чему равен z"))
    c = ("Ответ")
    d = ((x*y)/(g+z))
    string =c+" "+str(d)
    print(string)
def go():
    print("пиздуй в школу!")

def obr():
    Obraz = ("Образец:")
    print(Obraz)
    Zadacha = ("Дано уравнение (у/x)*(z/g), y-42, z-81, g-9. Найти х если ответ равен 54.")
    print(Zadacha)
    reshenie = ("Решение:")
    print(reshenie)
    primer_1 = ("Подставляем в пример значения y, z, g и получаем:")
    print(primer_1)
    primer_1_1 = ("(42/x)*(81/9)=54")
    print(primer_1_1)
    pri = (input("(81/9)="))
    if pri =="9":
        pr = (input("54/9="))
        if pr =="6":
            p = (input("42/6="))
            if p=="7":
                print("Молодец!")
            else:
                go()
        else:
            go()
    else:
        go()



# obr()
# xy()


# cars = {"opel":1000, "volvo":5000, "ford":10000}
# print(cars)
# print(cars["volvo"])
# cars['audi'] = 10500
# print(cars)
# del cars['ford']
# print(cars)


# person = {
#     "first name":"Volod'a",
#     "last name":"Schetinin",
#     "age":32,
#     "hobbies":["fart", "burp", "mace up"],
#     "children":"no children",
#     "car":"Rover",
# }
# print(person['first name'])
# print(person['last name'])
# print(person['age'])
# print(person['hobbies'])
# hobbies = (person["hobbies"])
# print(hobbies[2])
#
# print(person["hobbies"][1])
# print(person["children"])
# print(person['car'])

# tuple
# tuple_1 = (1, 3, 5)
# print(tuple_1)
# print(tuple_1[1])
# tuple_2 = (1, 2, 3, 4, 1, 7, 10)
# print(tuple_2.count(1))
# print(tuple_2.index(1))
# tuple_3 = ('vova', 'lop', 'sergo', 'kot', 'pet')
# print(tuple_3)
# print(tuple_3[3])
# print(tuple_3.index('lop'))
# print(tuple_3.count('lop'))

# set
# set_1 = {1, 2, 4, 5, 7, 89, 234, 457, 56567}
# print(set_1)
# lower = (584, 86498, 6, 547664)
# set_from_lower = set(lower)
# x = set_from_lower.pop()
# print(x)
# set_from_lower.remove(6)
# print(set_from_lower)
# set_from_lower.discard(4)
# print(set_from_lower)
# set_from_lower.add(777)
# print(set_from_lower)


# FOR.

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for y in x:
#     print(y)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for y in x:
#     if y % 2 == 0:
#         print(y)

# x = {('a', 'b'), ('c', 'd'), ('e', 'f')}
# for item, y in x:
#     print(item)
#     print(y)

# x = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
# for item in x.items():
#     print(item)
# for key, value in x.items():
#     print(key)
# for key, value in x.items():
#     print(value)
# for key, value in x.items():
#     print(key + value)
# for key, value in x.items():
#     print(key+" "+value)
# for item in x.keys():
#     print(item)
# for item in x.values():
#     print(item)



# WHILE.

# x = 0
# while x > 1:
#     print(x)
#     x -= 1

# while x <10:
#     print(str(x) + ' Hello world!')
#     x += 1
# print('new code')

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for item in x:
#     print(item)
#     pass
# print('bollen')

# for item in x:
#     if item == 2:
#         break
#     print(item)

# for item in x:
#     if item == 2:
#         continue
#     print(item)

# FUNCTIONS.

# def print_grit(name = 'Julia'):
#     print('Hello ' + name + ' !')
# print_grit('Jack')
# print_grit('loli')
# print_grit('Jane')

# def sum_number(a=0 , b=0):
#     return a+b
# x = sum_number(1, 2)
# print(x)

# def is_hello_in_text(text):
#     if 'hello' in text:
#         return True
#     else:
#         return False
print(is_hello_in_text('Say hello everyone.'))

# def is_hello_in_text(text):
#     if 'hello' in text:
#         return True
#     else:
#         return False
# print(is_hello_in_text('Say hello everyone.'))

