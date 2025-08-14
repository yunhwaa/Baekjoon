def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for p in range(len(phone_book)-1):
        if phone_book[p+1].startswith(phone_book[p]) == True:
            answer = False
    return answer