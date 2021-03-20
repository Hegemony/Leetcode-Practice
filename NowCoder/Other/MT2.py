while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            cnt += abs(i + 1 - nums[i])
        print(cnt)
    except EOFError:
        break