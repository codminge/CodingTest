def solution(arr1, arr2):
    arr1Len = len(arr1)
    arr2Len = len(arr2)
    sum1 = 0
    sum2 = 0
    if arr1Len > arr2Len:
        answer = 1
    elif arr1Len < arr2Len:
        answer = -1
    else:
        for i in range (0, arr1Len, 1):
            sum1 = sum1 + arr1[i]
            sum2 = sum2 + arr2[i]
            if sum1 > sum2:
                answer = 1
            elif sum1 < sum2:
                answer = -1
            else:
                answer = 0
    return answer