# Write a Python program to split a list based on first character of word

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
s=input("Enter the letter :")
m=[]
for ch in word_list:
    if ch[0]==s:
        m.append(ch)
print(m)    