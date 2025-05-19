#Print 1 to n using recursion

# def func(x,n):
#     if x>n:
#         return
    
#     print (x)
#     func(x+1,n)

# func(1,5)   


#TAIL (BACKTRACKING)
#Q-> Reverse a number using recursion with simple or something with the range 
def func(x,n):
    if x>n:
        return
    
    func(x+1,n)
    print(x)

func(1,5)
