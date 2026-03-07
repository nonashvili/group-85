#codewars 4
def likes(name):
    if len(name) == 0:
        return "no one likes this"
    elif len(name) == 1:
        return name[0] + " likes this"
    elif len(name) == 2:
        return name[0] + " and " + name[1] + " like this"
    elif len(name) == 3:
        return name[0] + ", " + name[1] + " and " + name[2] + " like this"
    else:
        return name[0] + ", " + name[1] + " and " + str(len(name) - 2) + " others like this"