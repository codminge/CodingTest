def solution(array, n):
    temp = 0
    tempList = []
    minimumList = []
    for i in array:
        if i >= n:
            temp = i - n
        else:
            temp = n - i
        tempList.append(temp)
    minTemp = min(tempList)
    if tempList.count(minTemp) > 1:
        restList = list(filter(
            lambda x: tempList[x] == minTemp, range(len(tempList))))
        for i in restList:
            minimumList.append(array[i])
        minimumList = sorted(minimumList)
        return minimumList[0]
    return array[tempList.index(minTemp)]