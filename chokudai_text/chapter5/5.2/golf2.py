# 数学的な解法

K = int(input())
A, B = map(int, input().split())

# 数学的な解法
ok = False

x = A // K
u = B // K

if x < u:
    ok = True

if A % K == 0:
    ok = True

if ok:
    print("OK")
else:
    print("NG")