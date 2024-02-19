def solution(arr):
    answer = 0
    while True:
        temp = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                temp.append(i / 2)
            elif i < 50 and i % 2 == 1:
                temp.append((i * 2) + 1)
            else:
                temp.append(i)
                
        if temp == arr:
            break
        else:
            answer = answer + 1
            arr = temp
            
    return answer