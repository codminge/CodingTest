def solution(arr):
    stk = []
    idx = 0
    stkIdx = -1
    
    while idx < len(arr):
        if len(stk) == 0:
            stk.append(arr[idx])
            idx = idx + 1
            stkIdx = stkIdx + 1
        elif len(stk) > 0 and stk[stkIdx] == arr[idx]:
            stk.pop()
            idx = idx + 1
            stkIdx = stkIdx - 1
        elif len(stk) > 0 and stk[stkIdx] != arr[idx]:
            stk.append(arr[idx])
            idx = idx + 1
            stkIdx = stkIdx + 1

    if len(stk) == 0:
        stk = [-1]
        
    return stk