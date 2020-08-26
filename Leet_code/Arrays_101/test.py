def find(x):
    if x.count(0) > 1:
        return True
    for i in x:
        if i != 0 and i * 2 in x:
            return True
    return False
a = [-2,0,10,-19,4,6,-8]
print(find(a))