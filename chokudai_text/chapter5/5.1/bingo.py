# 3×3のビンゴカード
bingo_card = []
for _ in range(3):
    row = list(map(int, input().split()))
    bingo_card.append(row)

# ３×3の判定カード（True,Flase）
bingo_check = []
for i in range(0, 3):
    row = []
    for j in range(0, 3):
        row.append(False)
    bingo_check.append(row)

# 抽選回数
N = int(input())

for _ in range(0, N):
    # 抽選番号
    select_num = int(input())

    # 抽選番号がビンゴカードにあるかの判定
    for i in range(0, 3):
        for j in range(0, 3):
            if bingo_card[i][j] == select_num:
                bingo_check[i][j] = True

bingo = False
M = bingo_check

# 横一列の確認
for i in range(0, 3):
    if M[i][0] and M[i][1] and M[i][2]:
        bingo = True
        print(f"横ビンゴ：{i+1}列目")

# 縦一列の確認
for i in range(0, 3):
    if M[0][i] and M[1][i] and M[2][i]:
        bingo = True
        print(f"縦ビンゴ：{i+1}列目")

# 斜め一列の確認
if M[0][0] and M[1][1] and M[2][2]:
    bingo = True
    print("斜めビンゴ：左上から右下")

if M[2][0] and M[1][1] and M[0][2]:
    bingo = True
    print("斜めビンゴ：左下から右上")

if bingo:
    print("BINGO!!")
else:
    print("NO BINGO!!")