def solution(strArr):
    dict = {}
    dictValuesList = []
    for i in strArr:
        count = 0
        if len(i) in dict:
            count = dict.get(len(i))
            count = count + 1
            dict[len(i)] = count
        else:
            count = count + 1
            dict[len(i)] = count
    for i in dict.values():
        dictValuesList.append(i)
    return max(dictValuesList)