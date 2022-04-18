A = [3,4,1,7,9,6]
def insertion_sort(A):
    for k in range (1, len(A)):
        cur = A[k]
        j = k
        while j>0 and A[j-1]>cur:
            A[j] = A[j-1]
            j -= 1
        A[j] = cur	 
def insertionSort(A):
    for i in range (1, len(A)):
        for j in range (i , 0 , -1):
            if A[j] < A[j-1]: # 왼쪽것이 더크면
                A[j],A[j-1] = A[j-1],A[j]
            else:
                break

print(A)
A = insertionSort(A)
print (A)