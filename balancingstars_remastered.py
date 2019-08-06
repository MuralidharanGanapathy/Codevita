def validate(close,open):
    if close == "}" and open == "{":
        return True
    if close == "]" and open == "[":
        return True
    if close == ")" and open == "(":
        return True
    return False
def rev_iter(s):
    for i in range(len(s)-1,-1,-1):
        if s[i] in ["{","[","("]:
            return i
    return -1
balance_counter = 0
ip = input()
stack = []
top = -1
open_is_there = 0
star_is_there = 0
ans = ""
flag = 0
for i in range(len(ip)):
    if ip[i] in ["[","(","{"]:
        stack.append(ip[i])
        top += 1
        open_is_there = 1
    elif ip[i] == "*" and top != -1:
        stack.append(ip[i])
    elif ip[i] == "*" and top == -1:
        flag = 1
    elif ip[i] in ["]",")","}"] and top != -1:
        if validate(ip[i],stack[top]) == True and len(stack) - top >= 2:
            del stack[top]
            balance_counter += 1
            top = rev_iter(stack)
        elif validate(ip[i],stack[top]) == False or len(stack) - top < 2:
            del stack[top]
            top = rev_iter(stack)
            flag = 1
    elif ip[i] in ["]",")","}"] and top == -1:
        flag = 1
if flag == 1:
    print("NO",balance_counter)
else:
    print("YES",balance_counter)
    
