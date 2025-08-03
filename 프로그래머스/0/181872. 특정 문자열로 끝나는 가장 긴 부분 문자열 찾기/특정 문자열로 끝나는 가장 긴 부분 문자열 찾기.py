def solution(myString, pat):
    answer = ''
    ans = 0
    for s in range(len(myString)):
        if myString[s:s+len(pat)] == pat:
            ans = s + len(pat)
    answer += myString[:ans]
    return answer