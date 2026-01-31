def count_even_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            count += 1
    print(count)

n = int(input("შეიყვანეთ მთელი რიცხვი: "))

count_even_numbers(n)
