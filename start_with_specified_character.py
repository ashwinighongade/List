# Write a Python program to find the items starts with specific character from a given list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# []
list=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

b=[]
c=[]
d=[]
for i in list:
    if i[0]=="a":
        b.append(i)
    if i[0]=="d":
        c.append(i)
    if i[0]=="w":
        d.append(i)
print(b)
print(c)
print(d)
