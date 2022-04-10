# Write a Python program to iterate a given list cyclically on specific index position. 
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']

list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b=0
i=0
while i<len(list):
    list1=list[3:]+list[:3]
    list2=list[5:]+list[:5]
    i+=1
print(list1)
print(list2)
 
