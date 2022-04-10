# Write a Python program to find the list with maximum and minimum length.
# Original list:
# num=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0]

# b=[]
# i=0
# c=[]
# # a=num[i]
# while i<len(num):
#     count=0
#     a=num[i]
#     j=0
#     while j<len(a):
#         count+=1
#         # print(count)
#         j+=1
#     b.append([count,num[i]])
    # c.append(count)
    
    # max=0
    # x=0
    # while i<len(c):
    #     if c[x]>max:
    #         max=c[x]
    #     x+=1
#     i+=1
# print(max)
# print(b)
# print(c)


num=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
count=1
count1=1
max=num[i]
min=num[i]
while i<len(num):
    if len(max)<len(num[i]):
        max=num[i]
        count+=1
    if len(min)>len(num[i]):
        min=num[i]
        count1+=1
    i+=1
print([count,max])
print([count1,min])        


    

