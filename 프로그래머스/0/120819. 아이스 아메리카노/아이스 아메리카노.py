def solution(money):
    answer = []
    n, left_money = 0, 0
    n = money // 5500
    left_money = money % 5500
    answer.append(n)
    answer.append(left_money)
    return answer