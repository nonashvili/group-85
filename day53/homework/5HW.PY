#CODEWARS 5
def distinct(seq):
    result = []
    for x in seq:
        if x not in result:
            result.append(x)
    return result