import numpy as np

def solution(num_list, n):
    idx = len(num_list)
    answer = np.array(num_list).reshape(idx//n, n)
    result = answer.tolist()
    return result