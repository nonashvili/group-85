#შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

names = ["data", "DOG", "Kaxa", "david", "Hello", "KING", "demo"]

new_list = []

for word in names:
    if word.lower() and word.startswith("d"):
        new_list.append("NIKA")
    elif word.upper() or word.startswith("K"):
        new_list.append("GOGA")
    else:
        new_list.append("ლიდერი")

print(new_list)