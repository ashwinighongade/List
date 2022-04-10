elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count=0
count1=0
count2=0
sum=0
sum1=0
sum2=0


i=0
while i<len(elements):
    count+=1
    sum=sum+elements[i]
    avg=sum/count
    if elements[i]%2==0:
        count1+=1
        sum1=sum1+elements[i]
        avg1=sum1/count1
        # print("sum number of ",elements[i])
    else:
        count2+=1
        sum2=sum2+elements[i]
        avg2=sum2/count2
        # print("odd number of ",elements[i])
    i+=1
print("sum of all elements :",sum)
print("avarge of all of elements",avg)
print("count of all number",count)
print("sum of sum number :",sum1)
print("sum of odd number :",sum2)
print("avarge of sum of number",avg1)
print("avarge of odd of number",avg2)
print("count of sum number",count1)
print("count of odd number",count2)











