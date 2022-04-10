# Python program to count the number of elements in a list within a specified range
list=[10,20,30,40,40,40,60,70,70,78,80,95,99]
count=0
i=0
while i<len(list):
    if list[i]>=40 and list[i]<=100:
        count+=1
    i+=1
print(count)
# count=0
# for x in list:
#     if x>=40 and x<=100:
#         count+=1
# print(count)

