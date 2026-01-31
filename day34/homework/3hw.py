def sum_of_even_numbers():
    numbers = [4, 7, 10, 3, 6, 9, 2]

    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num

    print("ლუწი ელემენტების ჯამი არის:", total)

sum_of_even_numbers()
