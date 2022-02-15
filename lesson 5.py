#s1="Hello\nworld"
#print(s1)
#r-/ знаки которые ствяться
# если в коде присутвуют знаки переноса
#или нужно вставить путь к чему ли бо
#\ знак переноса строки
#print(len(s1))
#индекс- это определение символа позиции в строке
#print(s1[3])#бдем "м" так как
#м третяя в слове "spams"счет идет от 0
#print(s1[2:4])
#print(s1[0:-2])
#print(s1[::-1])
#s2=0
#for letter in range(len(s1)-1):
#    s2=s2+letter
#    print(int(s2))
#print(s1[::2])#(от какой позиции:
# до какой позиции:убирает позиции в строке
# по счету "указаную")
import random
#print(random.random())
from random import randint,randrange #генераторы случайных чисел
#print("число",randint(0,9))#команда randint генерит
#случайное целое число в указаном диапазоне
#print("число",randrange(0,20))#
#city_list =["kartowka","morkovka","buriak"]
#print(city_list[random.randint(0, len(city_list))])
#print( "что то из списка-",random.choice(city_list))
#phase="что то из списка-"
#new_phase = phase.split("")
#print(random.choice(new_phase))

#list = [20,30,40,50,60,70,80,90]
#sampling = random.choices(list, k=3)
#print("число", sampling)#random.choices команда указывает скольок чисел
# из списка нужно вывести
#list=["Рубашка",
#      "Штаны",
#     "Футболка",
#     "Трусы",
#      "Кепка",
#     "Очки",
#     "Кеды"]
#print("Выбор из списка",random.choices(list, k=3))
#
#
n = int(input())
x = 1
i = 1
while i ** 2 <= n:
    x = i ** 2
    print(x)
    i += 1