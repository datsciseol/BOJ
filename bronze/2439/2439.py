star_num = int(input())
for i in range(star_num):
    print(" " * (star_num - 1 - i) + "*" *(i + 1))
