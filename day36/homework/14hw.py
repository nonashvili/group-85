def sumRange(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

print(sumRange(5, 100))
