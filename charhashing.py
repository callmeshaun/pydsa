#find q in s
#bRUTE FORCE METHOD
s="a Z @ y x y y z a a a a"
q=["a","a","y","z","Z","@"]

# hash_list=dict()

# for ch in s.split():

#     ascii_val=ord(ch)
#     index=ascii_val-97
#     hash_list[index]=hash_list.get(index,0)+1

# for ch in q:

#     ascii_val=ord(ch)
#     index=ascii_val-97
#     print(hash_list[index])

#DICTIONARY 
hash_list=dict()


for i in s.split():

    ascii=ord(i)
    index=ascii-127

    hash_list[index]=hash_list.get(index,0)+1

for i in q:

    ascii=ord(i)
    index=ascii-127

    print(hash_list[index])    



