while True:
    a, b = map(int, input().split())
    if a is 0 and b is 0:
        break
    else:
        if a > b:
            print("Yes")
        else:
            print("No")
