#HEAD RECURSION

# def func(x,n):
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)

# func(15,4)

#TAIL RECUSRION

def func(x,n):
    if n==0:
        return
    func(x,n-1)
    print(x)

func(15,4)    

