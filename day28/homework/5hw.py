total = 0

while True:
    number = int(input("shemoiyvane ricxvi 0 tu shemoiyvan dasruldeba: "))

    if number == 0:
        break

    if number > 0:
        print("dadebiti")
    else:
        print("uaryofiti")

    total += number

print("jami ari:", total)
