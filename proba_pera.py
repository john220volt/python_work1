def sum_nambers(n):
    summa = 0
    for i in range (1, n+1):
        summa += i
    print (summa)
sum_nambers(5)

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print(list_1[1])
#print(list_1[:3])
#print(list_1[2:])
#print(list_1.insert(5, 4))
print(list_1[len(list_1)-1])
print(list_1 [len(list_1)-2:])

t =  (1, 2, 3,)
print(type(t))