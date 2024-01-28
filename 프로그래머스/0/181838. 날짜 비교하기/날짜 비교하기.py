def solution(date1, date2):
    answer = 0
    for i in range(1, 3, 1):
        if len(str(date1[i])) == 1:
            date1[i] = '0' + str(date1[i])
        if len(str(date2[i])) == 1:
            date2[i] = '0' + str(date2[i])
    data1Str = "".join(map(str, date1))
    data2Str = "".join(map(str, date2))
    if data1Str < data2Str:
        answer = 1
    return answer