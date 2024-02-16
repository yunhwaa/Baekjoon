N = int(input())
num = int(input())
hap = num % 10
left = num // 10

for i in range(2, N+1):
  hap += left % 10
  left = left // 10


print(hap)