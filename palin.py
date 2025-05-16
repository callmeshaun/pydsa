def ispalin(n):
    num=n

    result=0
    while n!=0:

        ld=n%10
        result=ld+(result*10)
        n=n//10

    if num == result:
        print("Plaindrome")
    else:
        print("not palin")


ispalin(123)     
        