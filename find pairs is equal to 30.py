# How to find all pairs in an array of integers whose sum is equal to the given number?



number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==number:
            print(n[i],"and",n[j])

    

    