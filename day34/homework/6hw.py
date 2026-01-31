def find_longest_word():
    sentence = input("შეიყვანეთ წინადადება: ")

    words = sentence.split()
    i = 0
    longest_word = ""

    while i < len(words):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
        i += 1

    print("ყველაზე გრძელი სიტყვაა:", longest_word)

find_longest_word()
