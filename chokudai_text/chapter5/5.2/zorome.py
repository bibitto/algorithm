N = int(input())

a = int(N/9) # math.ceil(num)で小数点切り捨て
b = N % 9

result = []

for _ in range(0, a+2):
    if b == 0:
        result.append('9')
    else:
        result.append(str(b))

print(int("".join(result)))