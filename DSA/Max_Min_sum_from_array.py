def findSum(A,N): 
        #code here
        min = A[0]
        max = A[0]

        for i in range(0,N):
            if min < A[i]:
                min = A[i]
            else:
                pass
            if max>A[i]:
                max = A[i]
            else:
                pass
        return min+max

# def findSum(A,N):
#      return min(A)+max(A)


A = [-2, 1, -4, 5, 3]
N = len(A)
print(findSum(A,N))
