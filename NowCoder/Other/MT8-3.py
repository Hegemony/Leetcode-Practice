while True:
    try:
        a, b, c, d, e, f, g = list(map(int, input().split()))
        res = [[a, e], [b, f], [c, g]]
        res.sort(key=lambda x: (x[1]))
        # print(res)
        maxx = 0
        if d:
            if d and res[2][0]:
                if d >= res[2][0]:
                    maxx += res[2][1] * res[2][0]
                    d -= res[2][0]
                else:
                    maxx += d * res[2][1]
                    d = 0
            if d and res[1][0]:
                if d >= res[1][0]:
                    maxx += res[1][1] * res[1][0]
                    d -= res[1][0]
                else:
                    maxx += d * res[1][1]
                    d = 0
            # print('2:', maxx)
            if d and res[0][0]:
                if d >= res[0][0]:
                    maxx += res[0][1] * res[0][0]
                    d -= res[0][0]
                else:
                    maxx += d * res[0][1]
                    d = 0
            # print('3:', maxx)
        print(maxx)
    except EOFError:
        break