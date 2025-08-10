def solution(s):
    answer = True
    stack = []
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(s)):
        if s[0] != "(":
            answer = False
            break 
            
        if s[i] == ")":
            if len(stack) > 0:
                stack.pop()
            else:
                answer = False 
        else:
            stack.append(s[i])
    
    if len(stack) > 0:
        answer = False
    return answer