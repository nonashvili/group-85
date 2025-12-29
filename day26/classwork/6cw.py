list=[10, -5, 3, -1, 8, -2] 

i=0

for i in list:
    if i <0:
        list.remove(i)
print(list)