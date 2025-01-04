def solution(s):

    answer = ""  # 문자열은 더하기 사용하면 문자열 이어서 쓰는 것과 동일 -> 마지막에 int로 바꾸어 줌
    num_E_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']   # num_E_list의 인덱스 번호가 숫자와 동일하므로 숫자 리스트를 따로 만들어 줄 필요 X
    
    a = 0
    
    while a < len(s):   # 문자열 끝까지 반복
        if s[a].isdigit():   # 숫자인지 먼저 확인
            answer += s[a]
            a += 1
            
        else:   # 숫자가 아닐 경우
            for i in range(len(num_E_list)):
                if s[a:a + len(num_E_list[i])] == num_E_list[i]: 
                    answer += str(i)  # 인덱스 번호 문자열로 바꾸어서 더해줌
                    a += len(num_E_list[i])
                    break
            
    
    return int(answer)  # 수치형으로 바꿔서 출력


 

# 문자열로 초기화할 때는 0이 아닌 '' 사용!
# for문 루프 반복되지 않도록 break 사용!

# 딕셔너리 이용해서 푸는 방법도 있음! 

