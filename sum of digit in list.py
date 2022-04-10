# Find the sum of number digits in List.
# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]
# List Integer Summation : [6,9,2,9]
list=[12, 67, 98, 34] 
list2=[]  
i=0
while i<len(list):
    a=str(list[i])
    sum=0
    # sum=int(a[0])+int(a[1])
    j=0
    while j<len(a):
        sum=sum+int(a[j])
        j+=1
    list2.append(sum)
    i+=1
print(list2)


