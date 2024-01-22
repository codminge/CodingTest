import re

def solution(my_string):
    answer = []
    num = re.sub(r'[^0-9]', '', my_string)
    for i in num:
        answer.append(int(i))
    answer.sort()
    return answer