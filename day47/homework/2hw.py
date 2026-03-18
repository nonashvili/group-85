#codewars 2 hw 
def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    return sorted(a) == sorted(b)