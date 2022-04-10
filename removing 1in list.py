# The task is to perform the operation of removing all the occurrences of a given item/element present in a list.
# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :
# 2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
# After removing the item, the output list is [2, 3, 4, 5, 2]
# Input :
# 5 6 7 8 9 10
# 7
# Output :
# 5 6 8 9 10

# list = [1,1,2,3,4,5,1,2]
# b=[]
# i=0
# while i<len(list):
#     if list[i]==1:
#         pass
#     else:
#         b.append(list[i])
#     i+=1
# print(b)

# Remove empty List from List        
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

list=[5, 6, [], 3, [], [], 9]
b=[]
i=0
while i<len(list):
    if list[i]==[]:
        pass
    else:
        b.append(list[i])
    i+=1
print(b)
    






