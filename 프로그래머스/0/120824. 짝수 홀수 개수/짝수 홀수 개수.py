def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 1:
            odd = odd + 1
        else:
            even = even + 1
    return [even, odd]