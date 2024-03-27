menu = []
for i in range(1, 6):
  price = int(input())
  menu.append(price)

burger = min(menu[0], menu[1], menu[2])
drink = min(menu[3], menu[4])

print(burger + drink - 50)