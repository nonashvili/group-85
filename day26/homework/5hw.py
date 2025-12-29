#მომხმარებელს შემოაყვანინე რიცხვები, ეს რიცხვები დაამატე სიაში და გამოითვალე ამ რიცხვების საშუალო არითმეტიკული.

numbers = []

while True:
    user_input = input("შეიყვანე რიცხვი ან დაწერე 'stop': ")

    if user_input == "stop":
        break

    num = int(user_input)
    numbers.append(num)

average = sum(numbers) / len(numbers)

print("სია:", numbers)
print("საშუალო არითმეტიკული:", average)
