# write a code that finds second maximum element from the list and print it
number=[50,40,23,70,56,12,5,10,7]
# number.sort()
# print(number)
# number.pop()
# print(number)
# print("max value in the list=",max(number))

max=number[0]
smax=0
i=1
while i<len(number):
    if number[i]>max:
        max=number[i]
    print(max)
    i+=1
print(max)
# max=number[0]
# smax=0
# secondmax=0
# i=1
# while i<len(number):
#     if number[i]>max:
#         smax=max
#         max=number[i]
#         if max>smax and smax>number[i]:
#             secondmax+=smax
#     i+=1
# print(secondmax)
        
    # elif number[i]<max:
    #     smax=number[i]
    #     if max>smax and smax<=number[i]:
    #         print(smax)
    # i+=1


    # print(max)
    # i+=1
    # # print(max)

