    # Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:             
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             if (i!=j and j!=k and k!=i):
#                 print(i,j,k)

v=[1, 2, 3]
i=1

while i<=len(v):
    j=1
    while j<=len(v):
        k=1
        while k<=len(v):
            if (i!=j and j!=k and k!=i):
                print(i,j,k)
            k+=1
        j+=1
    i+=1