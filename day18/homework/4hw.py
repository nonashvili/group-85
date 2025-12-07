##მომხმარებელმა შეიყვანოს ტემპერატურა.
#თუ ტემპერატურა მეტია 0-ზე, შიგნით შეამოწმე:

 # თუ მეტია 30-ზე, დაბეჭდე "ცხელა"

 # თუ არა — "ნორმალურია"

#სხვა შემთხვევაში დაუბეჭდე - "ყინვაა"


temperature=int(input("enter temperature:"))

if temperature>0:
    if temperature>30:
        print("Cxela")
    else:
        print("normaluria")
else:
    print("yivaa")

