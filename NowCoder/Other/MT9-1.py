while True:
    try:
        n, m, a, b = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        nums.sort()
        res = [a, b]
        res.sort()
        minn = res[0]
        maxx = res[1]
        flag = 0
        cnt = 0
        for i in range(m):
            if nums[i] < minn:
                print('NO')
                flag += 1
                break
            elif nums[i] > maxx:
                print('NO')
                flag += 1
                break
            elif nums[i] == minn or nums[i] == maxx:
                cnt += 1
            elif minn < nums[i] < maxx:
                continue
        if n - m >= 2 - cnt and flag < 1:
            print('YES')
        elif flag < 1 and n - m < 2 - cnt:
            print('NO')
    except EOFError:
        break