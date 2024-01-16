def solution(num_list):
    idx = len(num_list)
    if num_list[idx-1] > num_list[idx-2]:
        num_list.append(num_list[idx-1] - num_list[idx-2])
    elif num_list[idx-1] <= num_list[idx-2]:
        num_list.append(num_list[idx-1] * 2)
    return num_list