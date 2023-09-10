
# Задание 1

print ("Введите монетки:\n")
n=input()

count_P=n.count('Р')
count_O=n.count('О')

if count_O>count_P: print (count_P)
else: print (count_O)

