N, Q = map(int, input().split())

# N×0の配列を作る（隣接リスト）
follow_situation = []
for i in range(0, N):
    row = []
    follow_situation.append(row)

# ログをもとにフォロー状況を復元
for i in range(0, Q):
    log = list(map(int, input().split()))

    if log[0] == 1:
        a = log[1]
        b = log[2]
        a -= 1
        b -= 1
        follow_situation[a].append(b)

    if log[0] == 2:
        a = log[1]
        a -= 1
        # 直前の記録を保存
        C = follow_situation
        for j in range(0, N):
            if a in C[j] and j not in C[a]:
                follow_situation[a].append(j)

    if log[0] == 3:
        a = log[1]
        a -= 1
        # 直前の記録を保存
        C = follow_situation
        for j in C[a]:
            print(f"{a+1}がフォロー：{j+1}")
            for k in C[j]:
                print(f"{j+1}がフォロー：{k+1}")
                if k not in C[a]:
                    follow_situation[a].append(k)

# 出力形式を問題に合わせる
result = []
for i in range(0, N):
    default_follow_status = "N "*N
    row = list(default_follow_status.split())
    result.append(row)

# フォロー状況をもとにresultを更新
for i in range(0, N):
    for j in follow_situation[i]:
        result[i][j] = "Y"
    print("".join(result[i]))
