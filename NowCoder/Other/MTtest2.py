while True:
    try:
        m, n = list(map(int, input().split()))
        res = []
        for i in range(m, n + 1):
            summ = 0
            temp = i
            while temp:
                summ += (temp % 10) ** 3
                temp //= 10
            if summ == i:
                res.append(i)
        if len(res) > 0:
            for i in range(len(res) - 1):
                print(res[i], end=' ')
            print(res[-1])
        else:
            print('no')
    except EOFError:
        break