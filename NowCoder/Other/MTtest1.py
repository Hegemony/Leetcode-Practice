import math

while True:
    try:
        n, m = list(map(int, input().split()))
        res = 0
        for i in range(m):
            if i == 0:
                res += n
            else:
                n = math.sqrt(n)
                res += n
        print('%.2f' % res)
    except EOFError:
        break
