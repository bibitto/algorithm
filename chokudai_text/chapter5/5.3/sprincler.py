# 隣接行列を使う場合

N, M, Q = map(int, input().split())

graph = []
for i in range(0, N):
    row = []
    for j in range(0, N):
        row.append(False)
    graph.append(row)

for i in range(0, M):
    u, v = map(int, input().split())
    # 番号をpythonのインデックスに合わせる
    u -= 1
    v -= 1
    # graphを更新する
    graph[u][v] = True
    graph[v][u] = True

# 各頂点の色の配列
C = list(map(int, input().split()))

# Q個のクエリを受け取る
for i in range(0, Q):
    query = list(map(int, input().split()))
    # スプリンクラーを起動する場合
    if query[0] == 1:
        x = query[1]
        x -= 1
        print(C[x])
        # 全ての頂点を順に見る
        for i in range(0, N):
            if graph[x][i]:
                C[i] = C[x]
    # スプリンクラーを起動しない場合
    if query[0] == 2:
        x = query[1]
        x -= 1
        y = query[2]
        print(C[x])
        C[x] = y