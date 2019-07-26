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
if ip[0] not in ["{","(","["]:
    flag = 1
for i in range(len(ip)):
    if ip[i] in ["(","{","["]:
        stack.append(ip[i])
        top = len(stack) - 1
        open_is_there = 1
    if ip[i] == "*" and open_is_there == 1:
        stack.append(ip[i])
        star_is_there = 1
    if ip[i] == "*" and open_is_there == 0:
        answer = "NO"
        star_is_there = 1
        continue
    if ip[i] in ["]",")","}"] and open_is_there == 0:
        answer = "NO"
        continue
    if ip[i] in [")","]","}"] and open_is_there == 1 and validate(ip[i],stack[top]) == True and len(stack)- top > 2:
        del stack[top:len(stack)]
        top = rev_iter(stack)
        balance_counter += 1
    elif ip[i] in [")","]","}"]:
        if open_is_there == 0 or validate(ip[i],stack[top]) == False or len(stack)- top <= 2:
            del stack[top:len(stack)]
            flag = 1
            top = rev_iter(stack)
            continue
if len(stack) == 0 and open_is_there == 1 and flag == 0 and star_is_there == 1:
    answer = "YES"
else:
    answer = "NO"
print(answer, balance_counter)
