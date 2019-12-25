sentence = input()
length = len(sentence)
if length % 10 is not 0:
    length = int(length/10) + 1
else:
    length = int(length/10)

for i in range(length):
    print(sentence[10 * i: 10 * i + 10 ])
