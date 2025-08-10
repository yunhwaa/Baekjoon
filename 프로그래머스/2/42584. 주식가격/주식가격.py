def solution(prices):
    answer = []
    price = 0

    for p in range(len(prices)):
        price = prices[p]
        time = 0
        for i in range(p+1, len(prices)):
            if prices[i] >= price:
                time += 1
            elif prices[i] < price:
                time += 1
                break
        answer.append(time)
    return answer