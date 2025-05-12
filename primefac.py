# Brute force Method
# def prime(num):

#     result=[]

#     for i in range(1,num+1):

#         if(num % i==0):

#             result.append(i)
#     return result

# print(prime(20)) 

#TC->O(N)
#SC->O(K) k->no of factors


#Better Solution

def prime(num):

    result=[]

    for i in range(1 , num//2):

        if(num % i==0):

            result.append(i)
    return result

print(prime(20))

#TC-> O(N)
#SC->O(1)



