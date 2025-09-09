def solution(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    answer = 0

    # 가장 무거운 사람과 가장 가벼운 사람 테우고 
    # 양 끝에서 시작해서 두 사람을 태울 수 있으면 같이, 아니면 무거운 사람만 태우는 방식 
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        answer += 1
    return answer