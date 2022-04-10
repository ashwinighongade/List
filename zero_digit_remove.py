# Write a Python program to move all zero digits to end of a given list of numbers. Go to the editor
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# b=[]
# c=[]
# list1=[]
# for i in list:
#     if i==0:
#         b.append(i)
#     else:
#         c.append(i)
#     list2=(c+b)
# print(list2)


list=[6,2,3,8]
min=list[0]
max=list[0]
for i in list:
    if i>max:
        max=i
    if i<min:
        min=i
b=[]
for s in range(min,(max+1)):
    b.append(s)
print(b)


    