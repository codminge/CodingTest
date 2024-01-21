def solution(array):
    mid = 0
    idx = len(array)
    array.sort()
    print(array)
    if idx % 2 == 0:
        mid = (array[int(idx/2)-1] + array[int(idx/2)]) / 2
    else:
        mid = array[int(idx/2)]
    return mid