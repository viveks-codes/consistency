arr = [-2, 1, -4, 5, 3]
n = len(arr)

def segregateElements(arr, n):
        l1 = []
        l2 = []
        for i in range(n):
            if arr[i]>=0:
                l1.append(arr[i])
            else:
                l2.append(arr[i])
        arr[:] = l1 + l2
        return l1+l2
print(segregateElements(arr, n))