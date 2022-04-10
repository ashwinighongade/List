# sort the list without using sort function


# num =[12,32,70,34,65,77,46,7]
# i=0
# while i<len(num):
#     j=0
#     while j<len(num):
#         if num[i]<num[j]:
#             num[i],num[j]=num[j],num[i]
#         j+=1
#     # print(num)
#     i+=1
# print(num)


num =[12,32,70,34,65,77,46,7]
i=0
while i<len(num):
    j=0
    while j<len(num):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
        j+=1
    # print(num)
    i+=1
print(num)

