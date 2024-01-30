def solution(array):
    answer = []
    dictionary = {}
    for i in array:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    for i in dictionary:
        answer.append(dictionary.get(i))
    if answer.count(max(answer)) >= 2:
        return -1
    for key, value in dictionary.items():
        temp = max(dictionary.values())
        if value == temp:
            return key