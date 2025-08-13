def solution(numbers):
    answer = ''
    nums = list(map(str, numbers))
    nums.sort(key = lambda x: x * 4, reverse=True)
    for n in nums:
        answer += n
    if int(answer) == 0:
        answer = '0'
    return answer