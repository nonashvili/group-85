def sumDigits(number):
    number = abs(number)  # ვიღებთ აბსოლუტურ მნიშვნელობას უარყოფითი რიცხვებისათვის
    total = 0

    for digit in str(number):
        total += int(digit)

    return total

print(sumDigits(1234))
print(sumDigits(9876))
print(sumDigits(-456))