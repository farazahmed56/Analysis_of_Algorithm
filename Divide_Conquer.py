# A = [8,3,1,5]

# minimum = A[0]
# maximum = A[0]

# for i in range(len(A)):
#     if A[i] < minimum: minimum = A[i]

#     if A[i] > maximum: maximum = A[i]

# print("Minimum: ", minimum)
# print("Maximum: ", maximum)

def minmax(A, i, j):
    #Only one element
    if i == j:
        return A[i], A[i]
    #Two elements
    elif i == j -1:
        if A[i] > A[j]:
            return A[j], A[i]
        else:
            return A[i], A[j]
    #More than two elements
    else: 
        mid = (i + j)//2
        min1, max1 = minmax(A, i, mid)
        min2, max2 = minmax(A, mid + 1, j)

    #finding overall max
    if max1 < max2:
        maximum = max2
    else:
        maximum = max1

    #finding overall minimum
    if min1 > min2:
        minimum = min2
    else: 
        minimum = min1

    return minimum, maximum

A = [5,10,1,2,8,4,3]
minimum, maximum = minmax(A, 0, len(A)-1)

print("Minimum: ", minimum)
print("Maximum: ", maximum)