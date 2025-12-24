#შექმენი list: animals = ["dog", "cat", "horse", "cow"] მომხმარებელს შეაყვანინე ცხოველის სახელი, თუ არსებობს  დაბეჭდე მისი index-იმ, თუ არა  "Animal not found"

animals = ["dog", "cat", "horse", "cow"]

user_animal = input("shemoyvane cxovelis saxeli: ")

if user_animal in animals:
    print(animals.index(user_animal))
else:
    print("Animal not found")
