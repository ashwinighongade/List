# Write a Code that finds second maximum element from the list and print it.

number = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# number.sort()
# print(number)
# print("Fist largest number in this list is :",number[-1])
# print("Second largest number in this list is :",number[-2])

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
print("first maximum number",max)
print("second maximum number",max1)



