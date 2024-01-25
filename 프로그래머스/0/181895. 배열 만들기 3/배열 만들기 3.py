def solution(arr, intervals):
    answer = []
    intervalsList = sum(intervals, [])
    for i in range(0, len(intervalsList), 2):
        answer = answer + arr[intervalsList[i]:intervalsList[i+1]+1]
    return answer