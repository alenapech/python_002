#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print('task 01')
n = input('Write a number: ')
sum = 0
for i in n:
    #if i.isdigit():
    if(i!='.' and i!=','):
        sum += int(i)
print(sum)
#print(sum([int(i) for i in input() if i.isdigit()]))

#2. Напишите программу, которая принимает на вход число N 
#  и выдает набор произведений чисел от 1 до N.
# n = int(input('Write a number: '))
# list = [1]
# for i in range(2, n+1):
#     list.append(i*list[i-2])  
# print(list)
print('task_02')
n = int(input('Write a number: '))
factorial = 1
#some_list=[]
for i in range (1, n + 1):
    #some_list.append(factorial*i)
    factorial *= i
    print(factorial, end = ' ')
#print(some_list)
print()

#3.Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
print('task_03')
n = int(input("Write a number: "))
some_dict = {}
sum = 0
for i in range(1, n + 1):
    sum = sum + round(((1 + 1/i)**i), 2)
    some_dict[i] = round(((1 + 1/i)**i), 2)
print(some_dict)
print(sum)

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
print('task_04')
from random import *
n = int(input())
some_list = [randint(-n,n) for _ in range(randint(5,10))]
print(some_list)

f = open('file.txt', 'w')
for i in range(randint(2, len(some_list))):
    f.write(str(randint(0, len(some_list) - 1)) + '\n')
f.close()

pr = 1
with open('file.txt', 'r') as f:
    for i in f.read().splitlines():
        pr = pr*some_list[int(i)]
print(pr)


#5. Реализуйте алгоритм перемешивания списка.
print('task_05')
from random import randint
list = []
for i in range(20):
    list.append(randint(-10, 10))
print(list)
import random 
random.shuffle(list)
print(list)