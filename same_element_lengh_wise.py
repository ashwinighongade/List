# Write a Python program to join two given list of lists of same length, element wise. 
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

list=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list1= [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
list2=[]
i=0
while i<len(list):
    c=list[i]+list1[i]
    list2.append(c)
    i+=1
print(list2)
    

list1=[1234,922,1984,19372,100]
b=str(list1[0])
a=b[0]
i=0
count=0
while i<len(list1):
    c=str(list1[i])
    if c[0]==a:
        count+=1
    i+=1
if count==5:
    print("True")
else:
    print("False")
