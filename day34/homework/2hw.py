def find_max_in_list():
    numbers = [3, 7, 2, 15, 9, 4]

    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

    print("სიის უდიდესი ელემენტია:", max_number)

find_max_in_list()
