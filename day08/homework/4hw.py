# მომხმარებელს შემოატანინე:
# --> ასაკი (age)
# --> სტუდენტია თუ არა (student) – შეიყვანოს "yes" ან "no"
# შემდეგ:
# თუ ასაკი ნაკლებია 12-ზე ან მეტია 65-ზე -> "ბილეთი უფასოა"
# თუ student == "yes" და ასაკი მეტია 12-ზე -> "ბილეთი ნახევარ ფასად"
# სხვა შემთხვევაში -> "სრული ფასი უნდა გადაიხადო"


age=int(input("please enter age:"))
student=input("yes or no:")
 

if age<12 or age>65:
     print("biletebi ufasoa")
elif student=="yes" and age>12:
      print("bileti naxevar pasad")
else:
      print("sruli pasi gadaixade")
    
