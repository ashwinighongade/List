# Find the First Maximum, Second maximum, Third maximum number from the List.
number=[12,43,23,22,67,45,89,54,34,73,11,92,7]
max=0
max1=0

i=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    if number[i]>max1:
        if number[i]!=max:
            max1=number[i]
    i+=1
max2=0
i=0
while i<len(number):
    if number[i]>max2:
        if number[i]!=max and number[i]!=max1:
            max2=number[i]
    # if number[i]>max2
    i+=1
print("First maximum number",max)
print("Second maximum number",max1)
print("Third maximum number",max2)











# max=0
# smax=0
# i=0
# while i<len(number):
#     if number[i]>max:
#         smax=max
#         max=number[i]
#     i=i+1
# print("first maximum number",max)
# i=0
# max1=0
# while i<len(number):
#     if number[i]>max1:
#         if number[i]!=max:
#             max1=number[i]
    
    # print(max)
    # i+=1
# print(smax)
# print("second maximum number",max1)
# i=0
# max2=0
# while i<len(number):
#     if number[i]>max2:
#         if number[i]!=max and number[i]!=max1:
#             max2=number[i]
#     i+=1
# print("Third max number",max2)

    

    



