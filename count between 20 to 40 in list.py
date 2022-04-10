#  count the number in the list between 20 to 40

number=[50,40,23,70,56,12,5,10,7]
# count=0
# for i in number:
#     if i>=20 and i<=40:
#         # count+=1
#         print(i)
#         count+=1
# print(count)
count=0
i=0
while i<len(number):
    if number[i]>=20 and number[i]<=40:
        print(number[i])
        count+=1
    i+=1
print("count",count)
