#codewars 4
def descending_order(num):
    s = str(num)             
    s = sorted(s, reverse=True) 
    s = "".join(s)            
    return int(s)        