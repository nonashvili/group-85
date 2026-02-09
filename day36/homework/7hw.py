def ricxvis_shefaseba():
    number = float(input("შეიყვანე რიცხვი: "))

    if number > 0:
        return "ეს რიცხვი დადებითია"
    elif number < 0:
        return "ეს რიცხვი უარყოფითია"
    else:
        return "ეს რიცხვი ნულია"

result = ricxvis_shefaseba()
print(result)
