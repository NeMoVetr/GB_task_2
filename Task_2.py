# Задание 2

print("Введите два числа X и Y:\n")
X=int(input())
Y=int(input())
flag=0
for i in range (1000):
    for j in range (1000):
        if i*j==Y and i+j==X and flag==0:
            flag=1
            print (i,j)