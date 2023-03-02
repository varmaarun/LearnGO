def tribonacci(signature, n):
    while n<3:
        signature.pop()
        n+=1
    if n>3:
        a,b,c=signature[0],signature[1],signature[2]
        i=3
        while i<n:
            a,b,c=b,c,a+b+c
            signature.append(c)
            i=i+1


    return signature



print(tribonacci([3, 2, 1], 10))