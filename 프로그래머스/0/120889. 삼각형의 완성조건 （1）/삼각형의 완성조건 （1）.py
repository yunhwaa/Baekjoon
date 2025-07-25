def solution(sides):
    answer = 2
    sides = sorted(sides, reverse=True)
    if sides[1] + sides[2] > sides[0]:
        answer = 1
    return answer