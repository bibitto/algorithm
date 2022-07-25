N = int(input())

A = []
for i in range(0, N):
    row = list(input())
    A.append(row)

ok = True

for i in range(0, N):
    for j in range(0, N):
        # i = jの時は調べない
        if i != j:
            if A[i][j] == "W":
                if A[j][i] != "L":
                    ok = False
            if A[i][j] == "L":
                if A[j][i] != "W":
                    ok = False
            if A[i][j] == "D":
                if A[j][i] != "D":
                    ok = False

if ok:
    print("correct")
else:
    print("incorrect")
