sleep_time = int(input())
wakeup_time = int(input())

time = (wakeup_time + 24) - sleep_time
if time == 24:
  time = 0
elif time > 24:
  time = time - 24
print(time)