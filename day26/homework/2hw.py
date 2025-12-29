# შექმენი ცარიელი სია. მომხმარებელს შეაყვანინე რიცხვები სანამ "stop"-ს არ დაბეჭდავს, ყოველი ახალი რიცხვი: თუ ნაკლებია 50-ზე → ჩასვი სიის დასაწყისში (insert), თუ მეტია ან ტოლია 50-ის → დაამატე ბოლოში (append), ბოლოს დაბეჭდე სია

numbers = []

while True:
    user_input = input("შეიყვანე რიცხვი ან დაწერე 'stop': ")

    if user_input == "stop":
        break

    num = int(user_input)

    if num < 50:
        numbers.insert(0, num)  
    else:
        numbers.append(num) 

print("საბოლოო სია:", numbers)
