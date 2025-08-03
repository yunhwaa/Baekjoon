def solution(seoul):
    answer = ''
    num = 0
    for s in range(len(seoul)):
        if seoul[s] == "Kim":
            num = s
    answer = "김서방은 " + str(num) + "에 있다"
    return answer