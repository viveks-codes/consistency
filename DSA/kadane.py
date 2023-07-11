arr = [1 ,2 ,3 ,-2 ,5]
N = 5

def maxSubArraySum(arr,N):
    summ = 0
    all_combo = []
    for i in range(N):
        for j in range(N+1):
            all_combo.append(arr[i:j])
    for k in all_combo:
        if k != []:
            print(sum(k))
        else:
            pass
maxSubArraySum(arr,N)