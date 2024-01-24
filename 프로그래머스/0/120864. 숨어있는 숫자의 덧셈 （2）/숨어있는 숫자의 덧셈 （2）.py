import re

def solution(my_string):
    answer = 0
    num = re.sub(r'[^0-9]', ' ', my_string)
    numList = num.split()
    for i in numList:
        answer = answer + int(i)
    return answer