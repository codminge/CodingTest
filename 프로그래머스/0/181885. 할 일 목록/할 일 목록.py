def solution(todo_list, finished):
    answer = []
    idx = len(todo_list)
    for i in range(0, idx, 1):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer