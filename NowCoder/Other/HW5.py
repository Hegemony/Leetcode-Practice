while True:
    try:
        s = input()
        res = set()
        flag = set()
        for i in range(len(s)):
            if s[i] not in flag:
                res.add((s[i], i))
                flag.add(s[i])
            else:
                continue
        res = list(res)
        res.sort(key=lambda x: [x[1]])
        c = ''
        for i in range(len(res)):
            c += res[i][0]
        print(c)
    except EOFError:
        break