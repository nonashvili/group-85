def udidesi_ricxvi(numbers):
    max_number = numbers[0]

    for ricxvi in numbers:
        if ricxvi > max_number:
            max_number = ricxvi

    return max_number


print(udidesi_ricxvi([3, 7, 1, 9]))
