#მომხმარებელს შემოაყვანინე რიცხვები, შექმენი ორი სია დადებითი და უარყოფითი სიებისთვის, დადებითი რიცხვები დაამატე დადებითი რიცხვებისთვის განკუთვნილ სიაში, უარყოფითი რიცხვები კი პირიქით

positive_numbers = []
negative_numbers = []

while True:
    user_input = input("შეიყვანე რიცხვი ან დაწერე 'stop': ")

    if user_input == "stop":
        break

    num = int(user_input)

    if num >= 0:
        positive_numbers.append(num)
    else:
        negative_numbers.append(num)

print(positive_numbers)
print(negative_numbers)
