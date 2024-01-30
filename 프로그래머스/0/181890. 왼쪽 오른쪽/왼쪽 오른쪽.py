def solution(str_list):
    if "l" in str_list and "r" in str_list:
        lIndex = str_list.index("l")
        rIndex = str_list.index("r")
        if lIndex < rIndex:
            return str_list[0:lIndex]
        else:
            return str_list[rIndex+1:len(str_list)]
    elif "l" in str_list:
        lIndex = str_list.index("l") 
        return str_list[0:lIndex]
    elif "r" in str_list:
        rIndex = str_list.index("r")
        return str_list[rIndex+1:len(str_list)]
    elif "l" not in str_list and "r" not in str_list:
        return []
