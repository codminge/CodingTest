def solution(str1, str2):
    a = list(str1)
    b = list(str2)
    c = list(zip(a, b))
    flat = []
    for sublst in c:
        flat.extend(sublst)
    return ''.join(flat)