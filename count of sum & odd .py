# Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
count1=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        count+=1
        
        print("sum number of ",elements[i])
    else:
        count1+=1
        print("odd number of ",elements[i])
    i+=1
print("count of sum :",count)
print("count of odd :",count1)