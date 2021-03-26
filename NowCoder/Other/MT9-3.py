while True:
    try:
        t = int(input())
        for _ in range(t):
            n = int(input())
            a = list(map(int, input().split()))
            dp1 = [a[0]]
            dp2 = [a[0]]
            summ = sum(a)
            for i in range(1, n):
                dp1.append(max(a[i], dp1[i - 1] + a[i]))
                dp2.append(min(a[i], dp2[i - 1] + a[i]))
            print(max(max(dp1), summ - min(dp2)))
    except EOFError:
        break
