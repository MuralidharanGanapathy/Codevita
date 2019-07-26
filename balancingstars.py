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
ans = ""
for i in range(len(ip)):
    if ip[i] in ["(","{","["]:
        stack.append(ip[i])
        top = i
        open_is_there = 1
    if ip[i] == "*" and open_is_there == 1:
        stack.append(ip[i])
    if ip[i] == "*" and open_is_there == 0:
        answer = "NO"
        continue
    if ip[i] in ["]",")","}"] and open_is_there == 0:
        answer = "NO"
        continue
    if ip[i] in [")","]","}"] and open_is_there == 1 and validate(ip[i],ip[top]) == True and i - top >= 2:
        del stack[top:i]
        top = rev_iter(stack)
        balance_counter += 1
    else:
        continue
if len(stack) == 0 and open_is_there == 1:
    ans = "YES"
else:
    ans = "NO"
print(ans, balance_counter)
        
