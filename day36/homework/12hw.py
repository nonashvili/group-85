def sumDigits(number):
    total=0

    for digit in str(number):
        total += int(digit)

    return total

print(sumDigits(1234))