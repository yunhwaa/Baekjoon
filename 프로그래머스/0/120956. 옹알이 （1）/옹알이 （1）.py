def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for w in words:
            babbling[i] = babbling[i].replace(w, ' ')
        babbling[i] = babbling[i].replace(' ', '')
    answer = babbling.count('')
    return answer




# def solution(babbling):
#     words = ["aya", "ye", "woo", "ma"]
#     for i in range(len(babbling)):
#         for word in words:
#             babbling[i] = babbling[i].replace(word, ' ')
#         babbling[i] = babbling[i].replace(' ', '')
#     return babbling.count('')