def solution(num_list):
    answer = 0
    oddJoin = ""
    evenJoin = ""
    idx = len(num_list)
    for i in range(0, idx, 1):
        if num_list[i] % 2 == 1:
            oddJoin = oddJoin + str(num_list[i])
        else:
            evenJoin = evenJoin + str(num_list[i])
    answer = int(oddJoin) + int(evenJoin)
    return answer