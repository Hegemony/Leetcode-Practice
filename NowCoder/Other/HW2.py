while True:
    try:
        n = int(input())
        res = set()
        for i in range(n):
            res.add(int(input()))
        res = list(res)
        res.sort()
        for i in range(len(res)):
            print(res[i])
    except EOFError:
        break
