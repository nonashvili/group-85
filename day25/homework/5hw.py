# შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება? (yes/no), თუ პასუხი "yes"  გამოიყენე clear(), ბოლოს დაბეჭდე list

nums = [1, 2, 3, 2, 4, 2, 5] 

user=input("yes or no:")
if user == "yes":
    nums.clear()

print(nums)