N = int(input())
ps = [0] + list(map(int, input().split()))

P = sum(ps)

# exist[i][s]: iまでの問題で得点合計をsにできる
exist = []
for i in range(N+1):
    exist.append([False]*(P+1))

# 初期条件
exist[0][0] = True

# iが小さい順にexistの値を求めていく
for i in range(1, N+1):
    for s in range(P+1):
        if exist[i-1][s]:
            exist[i][s] = True
        if s >= ps[i] and exist[i-1][s-ps[i]]:
            exist[i][s] = True

# 答えはexist[N][s]の中でTrueになっているs個数
ans = 0
for s in range(P+1):
    if exist[N][s]:
        ans += 1

print(ans)
