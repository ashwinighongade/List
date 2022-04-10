# Duplicates

a = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19]
# # Take out the duplicates from this list and put it in different list and print it.

b=[]
i=0
while i<len(a):
    n=a[i]
    j=0
    c=1
    while j<len(a):
        if a[i]==a[j] and i!=j:
            c+=1
        j+=1
    if c>1:
        if n not in b:
            b.append(n)
    i+=1
print(b)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
