# Write a Python program to convert a given list of strings into list of lists. 
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
list1=['Red', 'Maroon', 'Yellow', 'Olive']
list2=[]
for i in list1:
    for j in i:
        list2.append(j)
print(list2)
