remainder_list = []
for _ in range(10):
    remainder_list.append(int(input()) % 42)
print(len(set(remainder_list)))
