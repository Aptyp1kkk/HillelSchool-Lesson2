#new_list = [0,1,2,3,4]
#print(type(new_list))
#for number in new_list:
#    print (number)
#range-один из типа команды который автоматически
#считает от начального числа(заданого)
#до конечного (заданого)
#print(list(range(10,50)))
#for num in range(0.5):
#for num in range(5):
#    print(num)
#else:
#    print("числа закончились")
#print(len(list(range(10,50))))
#len-команда которая считает шаги
# в самом значении
#for num in range(10):
#    print(num)
#else:
#    print("числа закончились")
#for num in range(5):
#    if num ==3:
#        break
#break-используеться для прерывания в цикле
# какой либо инфо или слова
#    else:
#        print(num)
#else:сь")

#    print("числа закончились")

#i = 0 # переменая равна 0
#while i<5:# условие до которого будет идти цикл
#    print (i)
#    i +=1# присваивает +1 к предыдущему числу
#    # ( функция увеличения числа которое задано)
#else:
#    print("конец")

#i = 0
#while i<5:
#    if i ==3:
#        break
#    else:
#        print(i)
#    i +=1
#else:
#    print("конец")

#i = 0
#while i<5:
#    if i ==3:
#        i+= 1
#        continue
#    else:
#        print(i)
#    i +=1
#else:
#   print("конец")
#import time
#end_time = time. time() + 20
#while time.time() < end_time:
#    print("ok")
#   time.sleep(5)
#else:
#    print("Alarm")


n = int(input())
x = 1
y = 0
while x*2 <=n:
    x*=2
    y+=1
print(y,x)