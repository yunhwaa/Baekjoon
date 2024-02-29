N, K = map(int, input().split())

grade = [int(x) for x in input().split()]
grade.sort(reverse=True)
print(grade[K-1])