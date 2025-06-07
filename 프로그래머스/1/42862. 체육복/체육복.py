# reserve와 lost 비교
# -> lost 순차 탐색 (for문 사용)
# -> lost[i] 번호 +-1에 해당하는 번호가 reserve에 있으면 
#  count += 1
# 최종 answer: n - len(lost) + count

# 이거 젤 먼저! 
# reserve에 있는 학생이 lost에도 있으면 빌려줄 수 없음
# reserve에서 제거 
# 이 말의 의미! -> 자기 체육복을 도난당했지만 여벌이 있어서 입을 수 있음을 의미 
def solution(n, lost, reserve):
    answer = n - len(lost)
    count = 0
    
    lost.sort()
    reserve.sort()
    
    new_lost = []
    for l in lost:
        if l in reserve:
            reserve.remove(l)
            answer += 1  
        else:
            new_lost.append(l)
    
    for l in new_lost:
        if (l - 1) in reserve:
            reserve.remove(l - 1)
            count += 1
        elif (l + 1) in reserve:
            reserve.remove(l + 1)
            count += 1
    answer += count
    return answer
