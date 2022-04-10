# list1=[[2, 1], 2, 3, [2, 4], 5, 1]
# i=0
# b=[]
# while i<len(list1):
#     if type(list1[i])== list :
#         j = 0
#         while j < list1[i][0]:
#             b.append(list1[i][1])
#             j+=1
#     else:
#         b.append(list1[i])
#     i+=1
# print(b)
# Write a Python program to remove consecutive duplicates of a given list. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates.
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
# list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# b=[]
# for i in list:
#     if i not in b:
#         b.append(i)
# print(b)

# b=[] 
# i=0
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#     i+=1
# print(b)

# Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
list=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
b=[]
i=0
while i<len(list):
    j=0
    c=[]
    while j<len(list):
        if list[i]==list[j]:
            c.append(list[j])
    
        j+=1
    if c not in b:
        b.append(c)  
    i+=1
print(b)

        