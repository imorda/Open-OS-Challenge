from datetime import datetime

file = open('files.txt')
text = file.read()
file.close()

files = []

for i in text.split('\n'):
    tokens = []
    for j in i.split():
        tokens.append(j.strip())
    if len(tokens) == 0:
        continue
    # print(tokens)
    parsed = datetime.strptime(tokens[5] + " " + tokens[6].rstrip('0').rstrip('.'), '%Y-%m-%d %H:%M:%S')
    # print(parsed)
    files.append((parsed, tokens[-1]))

files.sort(reverse=True)
print(*files, sep='\n')
