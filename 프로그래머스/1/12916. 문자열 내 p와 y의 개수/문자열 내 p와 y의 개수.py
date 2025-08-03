def solution(s):
    answer = True
    s = s.lower()
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    num1 = s.count('p')
    num2 = s.count('y')
    if num1 != num2:
        answer = False

    return answer 