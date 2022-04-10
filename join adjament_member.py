# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']

list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
b=[]
while i<len(list)-1:
    add=list[i]+list[i+1]
    b.append(add)
    i+=1
print(b)    
    