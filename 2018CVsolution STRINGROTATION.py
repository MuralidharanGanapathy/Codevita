string_input = input()
s = ""
flag = 0
for _ in range(int(input())):
    direction, mag = input().split()
    if direction == "L":
        mag = int(mag) % len(string_input)
        s += string_input[mag]
    if direction == "R":
        mag = int(mag) % len(string_input)
        mag = -mag
        s += string_input[mag]
for i in range(len(string_input)-len(s)):
    if sorted(string_input[i:i+len(s)]) == sorted(s):
        print("YES")
        flag = 1
        break
if flag == 0:
    print("NO")
