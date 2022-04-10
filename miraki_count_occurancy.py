# Count Occurences
# Occurences - is made from the word occur which means that how many times a certain character or word appears.


char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
count=0
new=[]
i=0
while i<len(char_list):
    j=0
    c=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            c+=1
        j+=1
    if char_list[i] in new:
        i+=1
        continue
    new.append(char_list[i])
    print(char_list[i],"-",c)
print(new)


