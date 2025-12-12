#ტერმინალში გამკოიუტანეთ ყველა ლუწი რიცხვის ჯამი გამოიყენეთ ინდექსინგი

data = [10, 23, 35, 42, 58, 61]

sum_even = 0

for i in range(len(data)): 
    if data[i] % 2 == 0:     
        sum_even += data[i]

print(sum_even)
