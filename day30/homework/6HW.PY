words = ["apple", "banana", "kiwi", "orange", "pear", "grape", "melon"]

i = 0
while i < len(words):
    if len(words[i]) > 5 or i % 2 == 1:
        words.remove(words[i])
    else:
        i += 1

print(words)
