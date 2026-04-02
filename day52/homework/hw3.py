#codewars 3
def high_and_low(numbers):
    nlist = numbers.split()
    new_min = int(nlist[0])
    new_max = int(nlist[0])
    
    for i in nlist:
        num = int(i)
        if num > new_max:
            new_max = num
        elif num < new_min:
            new_min = num
            
    return f"{new_max} {new_min}"