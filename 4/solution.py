file = open('file.txt', mode='rb')
data = file.read()
file.close()

numbers = []

for i in range(0, len(data), 2):
    numbers.append(int.from_bytes(data[i:i+2], byteorder='big', signed=True))

print(len(numbers))

ans = 0
cur_len = 0
cur_symbol = -1
for i in numbers:
    if i == cur_symbol:
        cur_len += 1
    else:
        cur_symbol = i
        cur_len = 1
    if cur_len > ans:
        ans = cur_len

print(ans)
