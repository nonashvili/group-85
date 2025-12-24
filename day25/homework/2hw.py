#შექმენი list: fruits = ["apple", "banana", "apple", "orange"] მომხმარებელს შეაყვანინე ხილი, თუ list-ში უკვე არის ეს ხილი remove()-ით წაშალე მხოლოდ პირველი შემხვედრი, თუ არ არის ლისტში მაშინ დაბეჭდე შესაბამისი შეტყობინება

fruits = ["apple", "banana", "apple", "orange"]

user_fruit = input("შეიყვანე ხილი: ")

if user_fruit in fruits:
    fruits.remove(user_fruit)
    print("waishala es xili")
else:
    print("es araaaa listshii")

print("new:", fruits)
