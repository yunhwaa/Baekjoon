def solution(x):
    answer = False
    ans = 0
    x = str(x)
    for i in range(len(x)):
        ans += int(x[i])
    
    x = int(x)
    if x % ans == 0:
        answer = True
    return answer