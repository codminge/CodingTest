def solution(arr, queries):
    answer = []
    temp = 0
    for s, e, k in queries:
        for i in arr[s:e+1]:
            if k < i:
                if temp == 0:
                    temp = i
                else:
                    if temp > i:
                        temp = i
        if temp == 0:
            temp = -1
        answer.append(temp)
        temp = 0
    return answer