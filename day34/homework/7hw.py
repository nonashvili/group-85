def count_increases():
    numbers = [1, 3, 2, 5, 4]

    count = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            count += 1

    print(count)

# ფუნქციის გამოძახება
count_increases()
