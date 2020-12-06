def part_1():
    with open("input.txt") as f:
        ans = [line.replace("\n", "") for line in f.read().split("\n\n")]   
    s = 0
    group_ans = ""
    
    for group in ans:
        for letter in group:
            if letter not in group_ans:
                group_ans += letter
                
        s += len(group_ans)
        group_ans = ""
                    
    return s
    
def part_2():
    with open("input.txt") as f:
        ans = [i.split("\n") for i in [line for line in f.read().split("\n\n")]]   
    s = 0
    group_ans = ""
    
    for group in ans:
        for line in group:
            for letter in line:
                group_ans += letter
                
        ans_single = ""
        current = group_ans[0]
        for i in group_ans:
            if i not in ans_single:
                ans_single += i
                
        for i in ans_single:
            if group_ans.count(i) == len(group):
                s+=1
        group_ans = ""
        
    return s
    
print("day 1:", part_1())
print("day 2:", part_2())
