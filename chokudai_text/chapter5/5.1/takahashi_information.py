grid = []
for _ in range(0, 3):
    row = list(map(int, input().split()))
    grid.append(row)

# 矛盾を判断する変数
is_correct = True
C = grid

# 1,2列目の比較(b_1とb_2の差)
if C[0][0] - C[0][1] != C[1][0] - C[1][1] != C[2][0]- C[2][1]:
    is_correct = False

# 2,3列目の比較(b_2とb_3の差)
if C[0][1] - C[0][2] != C[1][1] - C[1][2] != C[2][1]- C[2][2]:
    is_correct = False

# 1,2行目の比較(a_1とa_2の差)
if C[0][0] - C[1][0] != C[0][1] - C[1][1] != C[0][2]- C[1][2]:
    is_correct = False

# 2,3行目の比較(a_2とa_3の差)
if C[1][0] - C[2][0] != C[1][1] - C[2][1] != C[1][2]- C[2][2]:
    is_correct = False

if is_correct:
    print("高橋は正しい")
else:
    print("高橋は嘘つき")