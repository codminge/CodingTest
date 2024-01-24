import re

def solution(my_string):
    answer = 0
    numList = re.findall(r'\d+', my_string)
    for i in numList:
        answer = answer + int(i)
    return answer