def solution(sizes):
    answer = 0
    size = sorted(sizes[0])
    h, w = size[0], size[1]
    for s in range(1, len(sizes)):
        size = sorted(sizes[s])
        h = max(h, size[0])
        w = max(w, size[1])
    answer = h * w
    return answer