
a = [3, 2, 5, 7, 8, 9, 1, 10, 9, 19, ]
print(a)
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
n = len(a)
print(n)

max = 1
lenght = 1
suma = 0
index = 0
for i in range(len(a)):
    if a[i] > a[i - 1]:
        lenght = lenght + 1
        if lenght > max:
            max = lenght
            suma = suma + a[i]
            print(index)
            index = index + (i + 1)
    else:
        lenght = 1
print(max)
print(suma)
print(index)






#
# x = 0
# for i in range(len(a)):
#     if a[i] < a[i + 1]:
#         x = x + i
#         print(a[i])
# print(x)
