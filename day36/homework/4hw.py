def didi_asoti_datsqebuli_sityvebi(words):
    result = []

    for word in words:
        if word and word[0].isupper():
            result.append(word)

    return result

words = ["თბილისი", "საქართველო", "კოდი", "Python", "python", "Usa"]
print(didi_asoti_datsqebuli_sityvebi(words))

