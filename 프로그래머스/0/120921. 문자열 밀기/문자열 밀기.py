def solution(A, B):
    answer = 0
    if A == B:
        answer = 0
        return answer

    for i in range(len(A)):
        ans1 = A[-i:] + A[:-i]
        if ans1 == B:
            answer = i
            break
        else:
            answer = -1
    return answer