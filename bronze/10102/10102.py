total_vote = int(input())
result = input()
a = 0
b = 0
for elem in result:
    if elem == "A":
        a += 1
    elif elem == "B":
        b += 1

if a > b:
    print("A")
elif a == b:
    print("Tie")
else:
    print("B")
