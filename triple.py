


firstnum=10
lastnum=99
count=0
while firstnum<lastnum:

    '''sstringnum=str(firstnum)
    if int(sstringnum[0]) - int(sstringnum[1]) == -3 or int(sstringnum[0]) - int(sstringnum[1]) == 3:
        print (sstringnum)'''
    if abs(firstnum//10 -firstnum%10)==3:
        print (firstnum)
        count=count+1
    
    firstnum=firstnum+1

print(count)