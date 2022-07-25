N = int(input())

S = []
for i in range(N):
    S.append(input())

C = {}
for string in S:
    if string in C:
        C[string] += 1
        count = str(C[string])
        print(string + '(' + count + ')')
    else:
        print(string)
        C[string] = 0