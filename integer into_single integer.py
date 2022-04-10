# Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
# Sample list: [11, 33, 50]
# Expected Output: 113350

list=[11, 33, 50]
string=""
for i in list:
    string=string+str(i)
print(string)
    