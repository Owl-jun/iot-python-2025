def solution(common):
    answer = 0
    if common[-2] - common[-1] == common[1] - common[0] : answer = common[-1] + (common[1]-common[0])
    else : common[-1] * (common[1] // common[0])
    return answer
    

print(solution([1,2,3,4]))
        
    