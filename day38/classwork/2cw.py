def is_even_or_not(number):
    if number % 2 == 0:
        return str(number) + "is even"
    elif number % 2 !=0:
        return str(number) + "is odd"
print(is_even_or_not(31))
print(is_even_or_not(323))
