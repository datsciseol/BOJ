star_num = int(input())
for i in range(star_num):
    print(" " * (star_num - i - 1) + "*" * (2 * i + 1))
    
