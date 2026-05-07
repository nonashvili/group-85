def number(lines):
    if lines==[]:
        return []
    
    result = []
    n=1
    
    for i in lines:
        result.append(str(n) + ": " + i )
        n +=1
        
    return result