count = int(input())
test = [int(count) for count in input().split()]
location = 0

for i in range(0, len(test)):
  location += test[i]

if location > 0:
  print("Right")
elif location == 0:
  print("Stay")
else:
  print("Left")