countries = ["Georgia", "USA", "france", "GERMANY", "Italy", "SPAIN"]

i = 0
while i < len(countries):
    if countries[i].upper():
        countries.pop(i)
    else:
        countries[i] = countries[i].upper()
        i += 1

print(countries)

