#შექმენით კალკულატორი როგორიც ჩვენ გავაკეთეთ,დაუმატეთ სხვა მათემატიკური ოპერატორები,ასევე დაუმატეთ შედარების ოპერატორებიც 


number1=int(input("enter any number:"))
number2=int(input("enter any number:"))
operator=input("enter + - * / ** % < > ")

if operator=="+":
    print(number1 + number2)
elif operator=="-":
    print(number1 - number2)
elif operator=="*":
    print(number1 * number2)
elif operator=="/":
    print(number1 / number2)
elif operator=="**":
    print(number1 ** number2)
elif operator=="%":
    print(number1 % number2)
elif operator=="<":
    print(number1 < number2)
elif operator==">":
    print(number1 > number2)
     