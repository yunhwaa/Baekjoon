def solution(polynomial):
    answer = ''
    a, b = 0, 0 
    poly = polynomial.split(' + ')
    for p in poly:
        if 'x' in p:
            if p == 'x':
                a += 1
            else:
                p = int(p[:-1])
                a += p
        else:
            b += int(p)
                
    if a != 0 and b != 0:
        if a == 1:
            answer = 'x + ' + str(b)
        else:
            answer = str(a) + 'x + ' + str(b)
    elif a == 0 and b != 0:
        answer = str(b)
    elif b == 0 and a != 0:
        if a == 1:
            answer = 'x'
        else:
            answer = str(a) + 'x'
    elif a == 0 and b == 0:
            answer = 0 
    return answer