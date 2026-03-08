import sys

dig = int(sys.argv[1])
base = int(sys.argv[2])

x = 1
ans = 0
num = 1


if dig < 0:
    x = -1
    dig = -dig

while dig > 0:
    ans += (dig % base) * num
    dig //= base
    num *= 10

ans *= x

print(ans)