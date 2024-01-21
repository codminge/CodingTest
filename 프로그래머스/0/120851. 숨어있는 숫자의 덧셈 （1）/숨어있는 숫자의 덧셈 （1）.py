import re

def solution(my_string):
    answer = 0
    num = re.sub(r'[^0-9]', '', my_string)
    for i in num:
        answer = answer + int(i)
    return answer