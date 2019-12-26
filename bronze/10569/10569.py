total_question = int(input())
for _ in range(total_question):
    v, e = map(int, input().split())
    print(e - v + 2)
