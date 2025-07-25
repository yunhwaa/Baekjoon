def solution(n, k):
    answer = 0
    k -= n // 10
    answer = 12000 * n + k * 2000
    return answer