def get_count(s):
    x="aeiou"
    amount=0
    for i in s:
        if i in x:
            amount+=1
    return amount
            