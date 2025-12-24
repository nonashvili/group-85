#შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი ლისტზე დიდია მაშინ გამოიყენე append()

nums = [1, 2, 3, 4]

indexi = int(input("shemoiyvane indqsio: "))
number = int(input("shemoiyvane ricxvi: "))

if 0 <= indexi <= len(nums) - 1:
    nums.insert(indexi, number)
else:
    nums.append(number)

print("new list:", nums)
