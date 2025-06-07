# 스택 이용해서 구현!
# number에 있는 수 stack에 넣고
# stack의 마지막에 있는 수가 더 작을 경우 pop()
# 그렇지 않으면 stack에 넣기 
# k - 1

# k가 0보다 크면 stack
def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k > 0:
        stack = stack[:-k]
    
    ans = ''
    for sta in stack:
        ans += sta
    return ans
        
    
        
    
    
