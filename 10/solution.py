file = open('img', encoding='ascii', errors='ignore')
text = file.read()
file.close()

ans = 0
for i in "AEIOUYaeiouy":
    ans += text.count(i)
print(ans)
