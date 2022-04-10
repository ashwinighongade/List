# Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
count1=0
sum=0
sum1=0

i=0
while i<len(elements):
    if elements[i]%2==0:
        count+=1
        sum=sum+elements[i]
        avg=sum/count
        # print("sum number of ",elements[i])
    else:
        count1+=1
        sum1=sum1+elements[i]
        avg1=sum/count1
        # print("odd number of ",elements[i])
    i+=1
print("sum of sum :",sum)
print("sum of odd :",sum1)
print("avarge of sum",avg)
print("avarge of odd of number",avg1)
print("count of sum number",count)
print("count of odd number",count1)


# its not work out check it 