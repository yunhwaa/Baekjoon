def solution(array, commands):
    ans = []
    l1 = []
    list1 = []
    
    for i in commands:
        l1 = i
        list1 = sorted(array[l1[0] - 1:l1[1]])
        ans.append(list1[l1[2] - 1])
    
    return ans