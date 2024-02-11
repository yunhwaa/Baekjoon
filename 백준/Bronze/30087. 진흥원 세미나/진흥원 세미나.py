list = {
    'Algorithm': '204',
    'DataAnalysis': '207',
    'ArtificialIntelligence': '302',
    'CyberSecurity': 'B101',
    'Network': '303',
    'Startup': '501',
    'TestStrategy': '105'
}

N = int(input())

for i in range(1, N+1):
  name = input()
  print(list[name])