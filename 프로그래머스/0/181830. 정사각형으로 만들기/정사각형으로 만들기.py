def solution(arr):
    answer = [[]]
    print(len(arr)) #행
    print(len(arr[0])) #열
    
    if len(arr) == len(arr[0]):
        answer = arr
    else:
        if len(arr) > len(arr[0]):
            temp = []
            for j in range(0, len(arr)-len(arr[0]), 1):
                temp.append(0)
            for i in arr:
                i.extend(temp)
            answer = arr
        elif len(arr) < len(arr[0]):
            for i in range(len(arr), len(arr[0]), 1):
                temp = []
                for j in range(0, len(arr[0]), 1):
                    temp.append(0)
                arr.append(temp)
            answer = arr
    return answer