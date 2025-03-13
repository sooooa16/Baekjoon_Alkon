n, m = map(int, input().split())
num = list(map(int, input().split()))
sum = 1

for i in num:
    sum = sum * (i % m)

print(sum%m)