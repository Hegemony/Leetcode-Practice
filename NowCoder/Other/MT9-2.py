while True:
    try:
        n, x = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        nums.sort(reverse=True)
        cnt = 0
        for i in range(n):
            if nums[i] >= nums[x - 1] and nums[i] != 0:
                cnt += 1
        print(cnt)
    except EOFError:
        break