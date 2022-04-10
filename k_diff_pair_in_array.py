nums=[3,1,4,1,5]
list=[]
for i in nums:
   if i not in list:
       list.append(i)
print(list) 
k=2
i=0
count=0
list1=[]
while i<len(list):
    j=0
    
    while j<len(list):
        if list[i]-list[j]== k:
            val=(list[i],list[j])
            # if (nums[i],nums[j]!=(nums[i],nums[j]):
            # list1.append(val)
            count+=1
            
        j+=1
    i+=1
print(list1)
print(count)


