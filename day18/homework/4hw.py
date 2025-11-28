##მომხმარებელმა შეიყვანოს ტემპერატურა.
#თუ ტემპერატურა მეტია 0-ზე, შიგნით შეამოწმე:

 # თუ მეტია 30-ზე, დაბეჭდე "ცხელა"

 # თუ არა — "ნორმალურია"

#სხვა შემთხვევაში დაუბეჭდე - "ყინვაა"


temperature=int(input("enter temperature:"))

if temperature>30:
    print("ცხელა")
elif temperature<30 and temperature>0:
    print("ნორმალურია")
else:
    print("ყინვაა")

