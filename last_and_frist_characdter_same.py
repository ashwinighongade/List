# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']

list=['abc', 'xyz', 'aba', '1221']
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count+=1
if count==len(list):
    print("c")
else:
    print("f")

