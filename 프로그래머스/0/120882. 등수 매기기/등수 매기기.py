def solution(score):
    rank = []
    temp = []
    for a, b in score:
        temp.append((a + b)/2)
    sorted_score = sorted(temp, reverse=True)
    for i in temp:
        tempRank = sorted_score.index(i) + 1
        rank.append(tempRank)
    return rank