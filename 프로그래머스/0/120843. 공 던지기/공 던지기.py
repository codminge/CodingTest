from collections import deque

def solution(numbers, k):
    answer = 0
    numbers = deque(numbers)

    i = 0
    while True:
        i += 1
        if k == i:
            return numbers[0]
        print(numbers.append(numbers.popleft()))
        print(numbers.append(numbers.popleft()))

    return answer