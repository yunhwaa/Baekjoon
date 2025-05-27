def solution(genres, plays):
    answer = []
    
    playlist = {}
    # 장르 선택 
    for g, p in zip(genres, plays):
        if g in playlist:
            playlist[g] += p
        else:
            playlist[g] = p
    
    sorted_playlist = dict(sorted(playlist.items(), key=lambda x: x[1], reverse=True))   # 내림차순 정렬
    
    genres_list = list(sorted_playlist.keys())
    
    for i in range(len(genres_list)):
        plays_num = {}
        n = 0
        for g in range(len(genres)):
            if genres_list[i] == genres[g]:
                plays_num[g] = plays[g]
        # plays_num: {고유번호: play재생횟수}
        # 재생횟수 많고(내림차순 정렬), 고유번호 작을수록(오름차순 정렬)
        sorted_plays_num = sorted(plays_num.items(), key=lambda x: (-x[1], x[0]))
        
        for n in range(min(2, len(sorted_plays_num))):
            answer.append(sorted_plays_num[n][0])
            
    return answer