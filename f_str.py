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

a = list(input().split())
for i in a:
    print(i)

a = input()
if a == 'Python':
    print('ДА')
else:
    print('НЕТ')