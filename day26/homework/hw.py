#შექმენი ცარიელი სია.მომხმარებელმა შეიყვანოს რიცხვები მანამ, სანამ არ დაწერს "stop".დაამატე მხოლოდ დადებითი რიცხვები სიაში, უარყოფითი რიცხვები არ დაამატო, ბოლოს დაბეჭდე სია

list = []

while True:
    user_input = input("შეიყვანე რიცხვი (stop გასაჩერებლად): ")

    if user_input == "stop":
        break

    list.append(int(user_input))

print("axali list:", list)
