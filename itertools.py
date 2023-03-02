from itertools import accumulate, combinations_with_replacement, permutations, product , combinations,accumulate,groupby
from multiprocessing.sharedctypes import Value

a=[1,2]
b=[3,4]

prod=product(a,b)

print(list(prod))

perm=permutations(a)

print(list(perm))

c=[1,2,3]
comp=combinations(c,2)
print(list(comp))

comp_wr=combinations_with_replacement(c,3)
print(list(comp_wr))


d=[1,2,3,4]
acc=accumulate(d)
print(list(acc))

def smaller_than(x):
    return x<3

group_obj=groupby(d,key=smaller_than)

for key, value in group_obj:
    print (key, list(value))