numb_list = []
for _ in range(5):
    numb_list.append(int(input()))

numb_list.sort()
print(sum(numb_list)//5)
print(numb_list[2])
