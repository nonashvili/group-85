#CODEWARS 4 
def number(lines):
    result = []
    for i in range(len(lines)):
        result.append(f"{i+1}: {lines[i]}")
    return result