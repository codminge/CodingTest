def solution(keyinput, board):
    answer = [0, 0]
    for i in keyinput:
        if i == "up":
            if (board[1] - 1) / 2 == answer[1]:
                answer[1]
            else: 
                answer[1] = answer[1] + 1
        elif i == "down":
            if -((board[1] - 1) / 2) == answer[1]:
                answer[1]
            else:
                answer[1] = answer[1] - 1
        elif i == "left":
            if -((board[0] - 1) / 2) == answer[0]:
                answer[0]
            else:
                answer[0] = answer[0] - 1
        elif i == "right":
            if (board[0] - 1) / 2 == answer[0]:
                answer[0]
            else:
                answer[0] = answer[0] + 1
    return answer