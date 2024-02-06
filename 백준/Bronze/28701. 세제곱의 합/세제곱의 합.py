N = int(input())
hap = 0
hap_3 = 0

for i in range(1, N+1):
  hap += i

hap_2 = hap*hap
print(hap)
print(hap_2)

for j in range(1, N+1):
  hap_3 += j*j*j

print(hap_3)