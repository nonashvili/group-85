# მომხმარებელს შემოატანინე:
# --> მომხმარებლის სახელი (username)
# --> პაროლი (password)
# შეამოწმე:
# თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
# თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
# სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!"




username=input("enter your name:")
password=input("please enter password:")

if username=="admin" and password=='superSecretPassword':
    print("mpgesalmebi admin")
else:
    print("momxmarebeli ar moidzebna")
    