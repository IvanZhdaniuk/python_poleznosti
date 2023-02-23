# print('число\t кважрат\t куб')
# for i in range(1, 11):
#     print(f'{i:2d}\t\t{i*i:3d}\t\t{i*i*i:4d}')
#
#
#
# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
#
# extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
# numbers.extend(extra)
# print(numbers)

# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
# sum_delit = 0
# sum_delit+= numbers.pop(-1)
# sum_delit+= numbers.pop(0)
# sum_delit+= numbers.pop(12)
# sum_delit+= numbers.pop(7)
# print(numbers)
# print(sum_delit)

# a, b = input().split()
# a =a.upper()
# a =list(a)
# b =b.upper()
# b = list(b)
# a = '-'.join(a)
# b = '-'.join(b)
# print(a, b)

# a = list(input().split())
# for i in a:
#     print(i)
#
# a = input()
# if a == 'Python':
#     print('ДА')
# else:
#     print('НЕТ')

# a = list(map(int, input().split()))
# if 3 in a:
#     a.remove(3)
# if 5 in a:
#     a.remove(5)
# if 7 in a:
#     a.remove(7)
# if 9 in a:
#     a.remove(9)
#
# print(a)


# if (a:=int(input())) <= 10000:
#     print(f'Сумма {a} не превышает лимит, проходите')
# else:
#     print(f'Ого! {a}! Куда вам столько? Мы заберем {a-10000}')

# chess bord

# a = input()
# b = input()
# chess = '_abcdefgh'
# if (int(chess.find(a[0])) + int(a[1]))%2 == 0 and int((chess.find(b[0])) + int(b[1]))%2 ==0 or\
#         int((chess.find(a[0])) + int(a[1]))%2 != 0 and int((chess.find(b[0])) + int(b[1]))%2 !=0:
#     print('YES')
# else:
#     print('NO')
#
# print(text := 'Even' if (int(input()) % 2) == 0 else 'Odd')


# print(text:='Even' if int(input())%2==0 else 'Odd')
#
# lang = input("Какой язык программирования будем учить?")
#
# match lang:
#     case "JavaScript":
#         print("Ты можешь стать фронтенд разработчиком")
#     case "Python":
#         print("Ты можешь стать Data Scientist-ом")
#
#     case "PHP":
#         print("Ты можешь стать бекенд разработчиком")
#
#     case "Solidity":
#         print("Ты можешь стать Blockchain разработчиком")
#
#     case "Java":
#         print("Ты можешь стать мобильным разработчиком")
#     case  _:
#         print("Язык не важен, главное уметь решать задачи)")

#
# numbers = [2, 3, 7, 9, 5, 0, 6, 3, 6, 0, 1, 7, 9, 4, 4, 4, 2, 2, 6, 9, 1, 7, 0, 3, 8, 1, 0, 3, 8, 0, 8, 4, 0, 2, 3, 6, 6, 1, 5, 8, 7, 2, 3, 8, 7, 7, 1, 2, 2, 8, 4, 3, 4, 8, 0, 7, 9, 8, 3, 7, 7, 7, 7, 5, 1, 7, 4, 5, 0, 8, 0, 9, 2, 4, 7, 6, 6, 5, 9, 7, 1, 7, 8, 8, 3, 4, 9, 7, 6, 4, 2, 0, 0, 0, 9, 4, 0, 9, 4, 4, 4, 5, 5, 4, 2, 5, 9, 4, 8, 1, 5, 7, 1, 0, 2, 6, 8, 7, 2, 7, 9, 3, 6, 4, 7, 5, 0, 7, 2, 0, 8, 2, 9, 8, 6, 4, 4, 7, 5, 5, 9, 4, 9, 5, 6, 9, 1, 1, 3, 1, 5, 2, 1, 7, 0, 0, 7, 8, 1, 3, 0, 0, 4, 4, 3, 3, 6, 7, 8, 6, 1, 2, 0, 2, 0, 9, 9, 0, 5, 2, 4, 1, 7, 4, 9, 9, 4, 9, 6, 9, 2, 7, 1, 2, 4, 5, 4, 0, 9, 0]
# while 4 in numbers:
#     numbers.remove(4)
#
# # здесь должен быть ваш код
# print(*numbers)
#
# b = 8
# while not int(str(b)[0]) == 1 or b > 1000000000:
#     b = b * int(str(b)[0])
# print(b)

# a = int(input())
# count = 0
# sum_bag = 0
# p = 0
# while a > sum_bag:
#     p = int(input())
#     if a >= (sum_bag + p):
#         sum_bag += p
#         count +=1
#     else:
#         print('Довольно!')
#         print(sum_bag)
#         print(count)
#         sum_bag +=p
#
# n, r = int(input()), []
# while sum(r) <= n:
#     r.append(int(input()))
# print('Довольно!', sum(r[:-1]), len(r) - 1, sep='\n')

# a_1, a_2 = 3, 5
# a = [2, 8, 8]
# b = [3, 4, 5, 5, 10]
# count_a = 0
# count_b = 0
# result = []
# while (a_1 - count_a) > 0 and (a_2 - count_b) > 0:
#     if b[count_b] >= a[count_a]:
#         result.append(a[count_a])
#         count_a += 1
#     elif b[count_b] <= a[count_a]:
#         result.append(b[count_b])
#         count_b += 1
# if count_a ==a_1 and count_b != a_2:
#     result += b[(count_b):]
# elif count_b ==a_2 and count_a != a_1:
#     result += a[(count_a):]
# for i in result:
#     print(i, end=' ')


# # Поиск делителей числа
# n = int(input())
# i = 1
# a = []
# while i*i <= n:
#     if n%i == 0:
#         if i == n//i:
#             a.append(i)
#         else:
#             a.append(i)
#             a.append(n//i)
#     i += 1
# a.sort()
# if len(a) == 2:
#     print('Yes')
# else:
#     print('No')
# print(sum(a))
#
# # Алгоритм Евклида:

# a = 35
# b = 5
#
# while b > 0:
#     c = a % b
#     a = b
#     b = c
# print(a)

# a = 75
# b = 120
# z = a * b
# while b > 0:
#     c = a % b
#     a = b
#     b = c
# z = z/a
# print(round(z))
#


# a = input()
# b = len(a) - 1
# count = 0
# while b > count:
#     if a[count] == 'e' or a[count] == 'a':
#         print('Ага! Нашлась')
#
#         print(a[count])
#
#         break
#     else:
#         print(f'Текущая буква: {a[count]}')
#         count += 1
#         print(a[count])
#
# else:
#     print('Распечатали все буквы')

# summa kubov

# summa_i = 0
# for i in range(50, 101):
#     print(summa_i :=summa_i + i*i*i)

# game in kubiki
# from random import randint
#
# a = int(input())
# count_mi = 0
# count_ci = 0
#
# for i in range(a):
#     mi = randint(1, 7)
#     ci = randint(1, 7)
#     print(mi, ci, end=' ')
#     print()
#     if mi > ci:
#         count_mi += 1
#     elif ci > mi:
#         count_ci += 1
# if count_ci > count_mi:
#     print('Chris')
#
# elif count_mi > count_ci:
#     print('Mishka')
# else:
#     print('Friendship is magic!^^')



# a = int(input())
# count = 0
# for i in range(a):
#     text = input()
#     count += 1
#     if 'рок' in text.lower():
#         print(count, text.lower().index('рок'))

# максимальное количество раз, которое встречается какая-либо буква (без учёта регистра) или иной символ во введённой
# строке.

# a = input().lower()
# max_count = 0
# for i in a:
#     if a.count(i) > max_count:
#         max_count=a.count(i)
# print(max_count)

# Для

# a = input()
# n = len(a)
# sum_nechet = 0
# sum_chet = 0
# nechet = a[0:n: 2]
# chet =a[1:n: 2]
# for i in nechet:
#     sum_nechet += int(i)
# for i in chet:
#     sum_chet += int(i)
# if (sum_nechet-sum_chet) % 11 == 0:
#     print('YES')
# else:
#     print('NO')

# a = input()
# count = 0
# pr = False
# for i in a:
#     if i == '(':
#         count += 1
#     elif i == ')':
#         count -= 1
#         if count < 0:
#             print('NO')
#             pr = True
#             break
# if count == 0 and pr == False:
#     print('YES')
# elif count != 0 and pr == False:
#     print('NO')

# На вход вашей программе поступает положительное целое число n, а ваша задача
# вывести в порядке возрастания все цифры, которые встречались в этом числе,
# и напротив каждого также необходимо вывести сколько раз данная цифра
# встречалась в числе n

# a = [4, 5, 6, 5, 4, 4]
# count =[0]*100
# print(count)
#
# for i in a:
#     count[i] += 1
# for j in count:
#     if j > 0:
#         print(j, count.index(j))


# Сортировка подсчетом
# Как видно из названия задачи, вам необходимо отсортировать список, состоящий только из чисел в пределах от -100 до 100 включительно, сортировкой подсчетом.
#
# Программа получает на вход число n - количество элементов в списке, затем сами элементы списка
#
# Вам необходимо вывести отсортированный список
#
# P.S. не пользуйтесь встроенной функцией sorted или методом sort

# b, a = input(), list(map(int, input().split()))
#
# count = [0] * 201
# for i in a:
#     count[i+100] += 1
#
#
# for i in range(201):
#     if count[i] > 0:
#         print((str(i-100)+' ' )*count[i], end='')
#
#
# Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20.
# count = 0
# count_2 = 0
#
# for i in range(1000, 10000):
#     count = 0
#     for j in str(i):
#         count += int(j)
#     if count == 20:
#         count_2 +=i
# print(count_2)

# сортировка пузырьком
#
# a =int(input())
# b = list(map(int, input().split()))
# count = 0
# for run in range(a-1):
#     for i in range(a-1-run):
#         if b[i] > b[i+1]:
#             b[i], b[i+1] = b[i+1], b[i]
#             count+=1
# print(*b)
# print(count)


#
# n, m = input().split()
# for a in range(1001):
#     for b in range(1001):
#         if a ** 2 + b == n and a + b ** 2 == m:
#             print(a, b)


# # сортировка вставками
#
# a = list(map(int, input().split()))
# n = len(a)
# for i in range(n - 1):
#     while a[i] > a[i + 1]:
#
#         a[i], a[i+1] = a[i+1], a[i]
#         if i>0:
#             i -= 1
#         print(a)

# Вам нужно посчитать сумму элементов двумерного квадратного (NxN)
# списка, которые расположены на главной диагонали.

# a = int(input())
# matrix = []
# summa = 0
# for i in range(a):
#     b = list(map(int, input().split()))
#     matrix.append(b)
#     summa += matrix[i][i]
# print(summa)

# work whith matrix
#
# a = int(input())
# matrix = []
# for i in range(a):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range(a):
#     for j in range(a):
#         print(matrix[j][i], end='')
#     print()

# a = int(input())
# matrix = []
# for i in range(a):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range(a-1, -1, -1):
#
#     for j in range(a-1, -1, -1):
#
#         print(matrix[j][i], end=' ')
#     print()

# a = list(map(int, input().split()))
#
# matrix = []
# for i in range(a[0]):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range(a[0]):
#
#     for j in range((a[1]-1), -1, -1):
#
#         print(matrix[i][j], end=' ')
#     print()

#
# a = list(map(int, input().split()))
#
# matrix = []
# for i in range((a[0]-1), -1, -1):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range((a[0]-1), -1, -1):
#
#     for j in range(a[1]):
#
#         print(matrix[i][j], end=' ')
#     print()

#
# Сумма строк и столбцов двумерного массива

# a = list(map(int, input().split()))
#
# matrix = []
# summa_columns = 0
# summa_columns_list = []
# summa_lines = 0
# summa_lines_list =[]
# for i in range((a[0])):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range((a[0])):
#     for j in range(a[1]):
#         summa_lines +=matrix[i][j]
#     summa_lines_list.append(summa_lines)
#     summa_lines = 0
# for i in range(a[1]):
#     for j in range(a[0]):
#         summa_columns += matrix[j][i]
#     summa_columns_list.append(summa_columns)
#     summa_columns = 0
#
# print(*summa_lines_list)
# print(*summa_columns_list)
#


# Симметричная ли матрица?

# a = int(input())
# matrix = []
# flag = True
# for i in range(a):
#     b = list(map(int, input().split()))
#     matrix.append(b)
# for i in range(a):
#     for j in range(a):
#         if matrix[i][j] == matrix[j][i]:
#             pass
#         else:
#             flag = False
# if flag==True:
#     print('Yes')
# else:
#     print('No')

#
# a, b = list(map(int, input().split()))
# matrix = []
# summa_broskov = 0
# summa_broskov_max = 0
# for i in range(a):
#     matrix.append(list(map(int, input().split())))
# for i in range(a):
#     for j in range(b):
#         summa_broskov += matrix[i][j]
#
#
#     if summa_broskov_max < summa_broskov:
#         summa_broskov_max = summa_broskov
#         pobeditel = i
#
#     summa_broskov = 0
# print(summa_broskov_max)
# print(pobeditel)

#
# a, b = list(map(int, input().split()))
# matrix = []
# max_brosok = 0
# broskov_max_dsave = 0
# for i in range(a):
#     matrix.append(list(map(int, input().split())))
# for i in range(a):
#     for j in range(b):
#         max_brosok = matrix[i][j]
#
#
#     if broskov_max_dsave < max_brosok:
#         broskov_max_dsave = max_brosok
#         pobeditel = i
#         popitca = j
#
#     max_brosok = 0
# print(broskov_max_dsave)
# print(pobeditel, popitca)


# a, b = list(map(int, input().split()))
# matrix = []
# max_brosok = 0
# broskov_max_dsave = 0
# summa_broskov = 0
# summa_broskov_dsave = 0
# count = 1
# for i in range(a):
#     matrix.append(list(map(int, input().split())))
# for i in range(a):
#     for j in range(b):
#         max_brosok = matrix[i][j]
#         summa_broskov += matrix[i][j]
#         if broskov_max_dsave < max_brosok:
#             broskov_max_dsave = max_brosok
#             pobeditel = i
#             popitca = j
#             max_brosok =0
#         elif broskov_max_dsave ==max_brosok:
#             count +=1
#     if count >1 and summa_broskov_dsave < summa_broskov:
#         summa_broskov_dsave = summa_broskov
#         pobeditel = i
#         popitca = j
#         summa_broskov= 0
# print(pobeditel)


# В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победитель определяется по лучшему результату. Определите количество участников состязаний, которые разделили первое место, то есть определите количество строк в массиве, которые содержат значение, равное наибольшему.
#
# Входные данные
#
# Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, являющихся элементами массива.
#
# Выходные данные
#
# Программа должна вывести  одно число - количество победителей соревнования.

#
# a, b = list(map(int, input().split()))
# matrix = []
# max_brosok = 0
# broskov_max_dsave = 0
# count = 1
# for i in range(a):
#     matrix.append(list(map(int, input().split())))
# for i in range(a):
#     for j in range(b):
#         max_brosok  = matrix[i][j]
#         if broskov_max_dsave < max_brosok:
#             broskov_max_dsave = max_brosok
#             pobeditel = i
#             popitca = j
#             max_brosok =0
#             count = 1
#         elif broskov_max_dsave ==max_brosok:
#             count +=1
#
# print(count)
#
#
# На днях Иван у себя в прихожей выложил кафель, состоящий из квадратных черных и белых плиток. Прихожая Ивана имеет квадратную форму 4х4, вмещающую 16 плиток. Теперь Иван переживает, что узор из плиток, который у него получился, может быть не симпатичным. С точки зрения дизайна симпатичным узором считается тот, который не содержит в себе квадрата 2х2, состоящего из плиток одного цвета.
#
# Примеры возможных узоров:
#
# Симпатичный узор
#
# По заданному расположению плиток в прихожей Ивана требуется определить: является ли выполненный узор симпатичным.
#
# Программе поступает на вход 4 строки по 4 символа «W» или «B» в каждой, описывающие узор из плиток. Символ «W» обозначает плитку белого цвета, а «B» - черного.
#
# Ваша задача вывести «Yes», если узор является симпатичным и «No» в противном
#
#
# flag =True
# matrix = []
# count = 1
# for i in range(4):
#     matrix.append(input())
# for i in range(1, 3, 1):
#     for j in range(1, 3, 1):
#         if matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i-1][j-1]and \
#         matrix[i][j] == matrix[i-1][j]:
#             flag =False
#         if matrix[i][j] == matrix[i-1][j] and matrix[i][j] == matrix[i-1][j+1]and \
#         matrix[i][j] == matrix[i][j+1]:
#             flag =False
#         if matrix[i][j] == matrix[i][j+1] and matrix[i][j] == matrix[i+1][j+1]and \
#         matrix[i][j] == matrix[i+1][j]:
#             flag =False
#         if matrix[i][j] == matrix[i][j-1] and matrix[i][j] == matrix[i +1][j] and \
#                 matrix[i][j] == matrix[i +1][j-1]:
#             flag = False
# if flag == False:
#     print('No')
# else:
#     print('Yes')


