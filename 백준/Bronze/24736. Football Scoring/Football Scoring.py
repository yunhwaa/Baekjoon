N = 5
visiting_team = [int(N) for N in input().split()]
home_team = [int(N) for N in input().split()]

score = [6, 3, 2, 1, 2]
score_A = 0
score_B = 0

for i in range(len(visiting_team)):
  score_A += visiting_team[i] * score[i]
  score_B += home_team[i] * score[i]

print("{} {}".format(score_A, score_B))