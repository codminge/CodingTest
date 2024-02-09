def solution(d, budget):
    answer = 0
    count = 0    
    d.sort()
    
    for i in range(0, len(d), 1):
        answer = answer + d[i]
        if answer > budget:
            break
        count = count + 1
        
    return count