#  palindrome word

# name= input("enter the name :")
# word=name[-1::-1]
# if name==word:
#     print("palindrome word")
# else:
#     print("not palindrome word")

# name=["m","a","d","a","m"]
# b=[]
# i=1
# while i<len(name)+1:
#     b.append(name[-i])
    
#     print(b)
#     i+=1
# if b==name:
#     print("its palindrome word")
# else:
#     print("its not palindrome word")

word=["madam"]
i=0
string=""
b=[]
while i<len(word):
    j=1
    while j<len(word[i])+1:
        string+=word[i][-j]
        j+=1
    i+=1
    b.append(string)
print(b)
if b==word:
    print("yes")
else:
    print("no")

