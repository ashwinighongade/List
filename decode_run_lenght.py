# Write a Python program to decode a run-length encoded given list. Go to the editor
# Original encoded list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Decode a run-length encoded said list:
# [1, 1, 2, 3, 4, 4, 5, 1]  

list1=[[2, 1], 2, 3, [2, 4], 5, 1]
i=0
b=[]
while i<len(list1):
    if type(list1[i])== list :
        j = 0
        while j < list1[i][0]:
            b.append(list1[i][1])
            j+=1
    else:
        b.append(list1[i])
    i+=1
print(b)

# Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]

# list=[1, 1, 2, 3, 4, 4, 5, 1]
# b=[]
# i=0
# while i<len(list):
#     if list[i]!=2:
#         b.append(list[i])
#     i+=1
# print(b)

# list=[1, 1, 2, 3, 4, 4, 5, 1]
# b=[]
# i=0
# while i<len(list):
#     if list[i]==list[2]:
#         b.append(12)
#     else:
#         b.append(list[i])
        
        
#     i+=1
# print(b) 

      
list=[1, 2, 3, 4, 5, 6, 7, 8, 9]
b=[]
i=0
while i<len(list):
    j=1
    while j<len(list):
        # a=list[i+1]
        b.append([list[i],list[j]])
        j+=1
    i+=1
# print(b)