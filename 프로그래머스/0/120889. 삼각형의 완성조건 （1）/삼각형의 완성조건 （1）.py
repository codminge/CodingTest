def solution(sides):
    sumSides = 0
    maxSides = max(sides)
    for i in sides:
        sumSides = sumSides + i
    sumSides = sumSides - maxSides
    if sumSides > maxSides:
        return 1
    else:
        return 2