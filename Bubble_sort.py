A = [21,19,12,26,8,9,3,2,0,11,]
n = len(A)

for i in range(n-1):
    for j in range(n-1):
        if A[j] > A[j+1]:
            #swap
            A[j], A[j+1] = A[j + 1], A [j]
print("Sorted Array: ", A)