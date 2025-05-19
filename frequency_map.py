# nums = [1, 2, 3, 4, 4, 2, 1, 5, 5, 1, 4, 3]

#METHOD 1

# freq_map = dict()

# for i in range(0, len(nums)):

#     if nums[i] in freq_map:

#         freq_map[nums[i]]+=1 

#     else:

#         freq_map[nums[i]] = 1

# print(freq_map[1])

# TC->O(N)
# SC->O(N)=worst case deped on numbers

# Method 2

# hash_map={}

# n=len(nums)

# for i in range(0,n):

#     hash_map[nums[i]]= hash_map.get(nums[i],0)+1

# print(hash_map[1])

#TC->O(1)

#Find m in n 
#Brute force method quick method which came in my mind

# n =[5,3,2,2,1,5,5,7,5,10]
# m =[10,111,1,9,5,67,2]

# for num in m:
#     count =0

#     for x in n:

#         if x==num:
#             count+=1
#     print(count)      

#OPTIMAL METHOD

# hash_list=[0]*11

# for num in n:
#     hash_list[num]+=1

#     for num in m:
#         if num<1 or num>10:
#             print(0)
#         else:
#             print(hash_list[num])    

#USING DICTIONARY

# hash_map=dict()
# nums=len(n)

# for i in range(0,nums):

#     hash_map[n[i]]= hash_map.get(n[i],0)+1

# for num in m:

#  print(hash_map.get(num,0))
