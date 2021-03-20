while True:
    try:
        n, x, y = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        if x * 2 > n or y * 2 < n:
            print(-1)
        nums.sort()
        res = []
        for i in range(n):
            res.append(nums[i])
            if x <= len(res) <= y and x <= (n - i + 1) <= y:
                break
        if len(res) != n:
            print(res.pop())
        else:
            print(-1)
    except EOFError:
        break