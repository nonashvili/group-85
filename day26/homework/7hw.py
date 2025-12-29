#მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში, თუ ორი მეზობელი ელემენტის ჯამი <50-ზე მაშინ წაშალე მეორე ელემენტი, დაბეჭდე საბოლოო სია.

numbers = []

while True:
    user_input = input("შეიყვანე რიცხვი ან დაწერე 'stop': ")

    if user_input == "stop":
        break

    numbers.append(int(user_input))

i = 0
while i < len(numbers) - 1:
    if numbers[i] + numbers[i + 1] < 50:
        numbers.pop(i + 1) 
    else:
        i += 1

print(numbers)
