def solution(before, after):
    answer = 0
    dictionaryBefore = {}
    dictionaryAfter = {}
    for i in before:
        key, value = i, before.count(i)
        dictionaryBefore[key] = value
    for k in after:
        key, value = k, after.count(k)
        dictionaryAfter[key] = value
    if dictionaryBefore == dictionaryAfter:
        answer = 1
    return answer