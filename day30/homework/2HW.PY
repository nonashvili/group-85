words = ["hello", "World", "python", "Code", "test", "DATA"]

i = 0
while i < len(words):
    if words[i].lower():
        words[i] = words[i].upper()
        i += 1
    else:
        words.pop(i)

print(words)