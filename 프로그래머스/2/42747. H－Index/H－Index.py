def solution(citations):
    h = 0
    ans = []
    n = 1
    citations.sort(reverse=True)
    
    for num in citations:
        if num >= n:
            h = n
            n += 1
            ans.append(h)
            
    if len(ans) == 0:
        return 0
     
    return ans[-1]

