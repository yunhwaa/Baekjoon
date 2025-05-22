# numbers의 원소는 0 이상 1000이하라는 제한사항! 
def solution(numbers):
    ans = ''
    num = list(map(str, numbers))
    
    num.sort(key = lambda x: x*3, reverse=True)
    ans = str(int("".join(num)))
    
    
    return ans