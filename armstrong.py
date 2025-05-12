def isArm(num):

    nod = len(str(num))
    n=num
    total=0

    while n>0:

        ld=n%10
        total=total + (ld**nod)
        n=n//10
    return total==num

print(isArm(1234))