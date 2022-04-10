# Write a Python program to compute the average of nth elements in a given list of lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]

a=[[0, 1, 2],
    [2, 3, 4], 
    [3, 4, 5, 6], 
    [7, 8, 9, 10, 11],
    [12, 13, 14]]
li=[]
exist=True
j=0
while exist:
  sum=0
  count=0
  for i in a:
    if j<len(i):
      count+=1
      sum+=i[j]
  if sum==0:
    exist=False
  else:
    # print(sum)
    # print(count)
    # print()
    li.append((sum/count))
  j+=1
print(li)


# b=[]
# c=[]
# i=0
# while i<5:
#   name=input("Entet the name :")
#   b.append(name)
#   i+=1
# x=1
# while x<len(b)+1:
#   c.append(b[-x])
#   x+=1
# print(c)
    