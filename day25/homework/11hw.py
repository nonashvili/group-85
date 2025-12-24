 #შექმენი ცარიელი list მომხმარებელს შემოაყვანინე რიცხვები მანამ სანამ არ დაწერს "stop", ყველა რიცხვი დაამატე ლისთში append()ის გამოყენებით და საბოლოოდ დაბეჭდე ლისთი

list = []

while True:
    user_input = input("შეიყვანე რიცხვი (stop გასაჩერებლად): ")

    if user_input == "stop":
        break

    list.append(int(user_input))

print("axali list:", list)
