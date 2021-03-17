while True:
    try:
        n = int(input())
        if n > 1000:
            n = 999
        i = 0
        res = [i for i in range(n)]
        while len(res) > 1:
            i += 2
            i %= len(res)
            res.remove(res[i])
        print(res[0])

    except EOFError:
        break
