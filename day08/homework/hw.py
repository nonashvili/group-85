#მომხმარებელს შემოატანინე ტემპერატურა (რიცხვი) და შემდეგ შეამოწმე:
# თუ ტემპერატურა მეტია 30-ზე -> დაბეჭდე "ძალიან ცხელა!"
# თუ ტემპერატურა მეტია 20-ზე -> დაბეჭდე "სასიამოვნო ამინდია"
# თუ ტემპერატურა მეტია 10-ზე -> დაბეჭდე "ცოტა ცივა"
# თუ ტემპერატურა მეტია 0-ზე -> დაბეჭდე "ცივა, ჩაიცვი თბილად"
# სხვა შემთხვევაში -> "გაიყინები, სახლში დარჩი!"



temperature=int(input("enter number:"))

if temperature>30:
    print("dzaan cxela")
elif temperature>20:
    print("sasiamovno amindia")
elif temperature>10:
    print("cota civa")
elif temperature>0:
    print("civa tbilad chaicvi")
else:
    print("saaxshi darchi gaiyinebi")