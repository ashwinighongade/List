# Write a Python program to check if first digit/character of each element in a given list is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if the first digit in each element of the given list is the same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False

list1=[1234, 122, 1984, 19372, 100]
i = 0 
while i < len(list1):
    if type(list1[i]) == int or float:
        a = str(list1[i])
    else:
        a = list1[i]
    j = 0
    c = 0
    while j < len(list1):
        if type((list1[j])) == int or float:
            b = str(list1[j])
        else:
            a = list1[j]
        if a[0] == b[0]:
            c+=1
        j+=1
    if c == len(list1):
        print(True)
    else:
        print(False)
    break
    i+=1
            
# list=['aabca', 'abca', 'aba', 'ahaca']
# i=0
# while i<len(list):
#     j=0
#     count=0
#     while j<len(list):
#         if list[j][0]==list[j][-1]:
#             count+=1
#             # print(True)
#         # else:
#         #     # False
#         j+=1
        
#     i+=1
# print(count)

