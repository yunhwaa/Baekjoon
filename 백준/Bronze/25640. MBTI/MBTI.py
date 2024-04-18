my_MBTI = input()
N = int(input())
count = 0

for i in range(0, N):
  MBTI = input()
  if MBTI == my_MBTI:
    count += 1
print(count)