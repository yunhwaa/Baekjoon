N = 3
num = [int(N) for N in input().split()]
num.sort()
print("{} {} {}".format(num[0], num[1], num[2]))