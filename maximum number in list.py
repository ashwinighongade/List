# write a code that print the maximum in this list
number=[50,40,23,70,56,12,5,10,7]
# print("maximum number in this list=",max(number))
max=0
# smax=0
i=0
while i<len(number):
    if number[i]>max:
        # smax=max
        max=number[i]
    i=i+1
print("first maximum number",max)
i=0
max1=0
while i<len(number):
    if number[i]>max1:
        if number[i]!=max:
            max1=number[i]
    
    # print(max)
    i+=1
# print(smax)
print("second maximum number",max1)
i=0
thirdmax=0
while i<len(number):
    if number[i]>thirdmax:
        if number[i]!=max and number[i]!=max1:
            thirdmax=number[i]
    i+=1
print("Third max number",thirdmax)
