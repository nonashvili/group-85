
text = "PyThOn"
result = []

i = 0
while i < len(text):
    if text[i].upper():
        result.append(text[i].lower())
    elif text[i].lower():
        result.append(text[i].upper())
    i += 1

print(result)
