from itertools import permutations

def solution(numbers):
    nums = set()
    
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            nums.add(int(''.join(p)))
    
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

    return sum(1 for n in nums if is_prime(n))