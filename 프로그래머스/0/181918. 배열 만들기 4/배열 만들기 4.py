def solution(arr):
    stk = []
    arridx = len(arr)
    i = 0
    while i < arridx:
        stkidx = len(stk)
        if stkidx == 0:
            stk.append(arr[i])
            i = i + 1
        else:
            if stk[stkidx-1] < arr[i]:
                stk.append(arr[i])
                i = i + 1
            else:
                stk.remove(stk[stkidx-1])
    return stk