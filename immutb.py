def append_to(element, to=None):
    if to==None:
        to=[]   
    to.append(element)
    return to

print(append_to(2))
print(append_to(22))