# Write a Python program to get the difference between the two lists. 

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
# output=[9,3,5,8,2,4,6]
# diff_list1_list2 = list(set(list1) - set(list2))
# diff_list2_list1 = list(set(list2) - set(list1))
# total_diff = diff_list1_list2 + diff_list2_list1
# print(total_diff)
b=[]
c=[]
for i in list1:
    if i not in list2:
        b.append(i)
for x in list2:
    if x not in list1:
        c.append(x)
    d=b+c
print(d)
    
    
# Write a Python program to compute the difference between two lists. Go to the editor
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
# color=["red", "orange", "green", "blue", "white"]
# color1= ["black", "yellow", "green", "blue"]
# b=[]
# c=[]
# for i in color:
#     if i not in color1:
#         b.append(i)
# for x in color1:
#     if x not in color:
#         c.append(x)
# print(b,c)

