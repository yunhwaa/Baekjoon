def solution(lines):
    answer = 0
    ans_list = []
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            start = max(lines[i][0], lines[j][0])
            end = min(lines[i][1], lines[j][1])
            if start < end:
                for n in range(start, end):
                    ans_list.append(n)
    ans_list = list(set(ans_list))
    answer = len(ans_list)
    return answer