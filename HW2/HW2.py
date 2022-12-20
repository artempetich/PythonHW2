# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

sum_digits = 0
n = input("Ведите вещественное число: ")
for i in n:
    if i.isdigit():
        sum_digits += int(i)
print(sum_digits)





# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

#n = int(input("Ведите число: "))
#list_numbers = []
#summ = 0
#for i in range(1, n+1):
    #value = (1+1/i)**i
    #list_numbers.append(value)
    #summ += value
#print(list_numbers)
#print(summ)



# Реализуйте алгоритм перемешивания списка.
#import random

#initial_list = [1,2,3,4,5,6,7]
#new_list = initial_list
#for _ in new_list:
    #index_1 = random.randrange(len(new_list))
    #index_2 = random.randrange(len(new_list))
    #temp = new_list[index_1]
    #new_list[index_1] = new_list[index_2]
    #new_list[index_2] = temp
#print(new_list)