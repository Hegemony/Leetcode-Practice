while True:
    try:
        n = int(input())
        s = input().split()
        ss = s[0]
        cnte, cntf = 0, 0
        dp = [0 for i in range(n)]
        for i in range(n):
            if ss[i] == 'E':
                cnte += 1
            elif ss[i] == 'F':
                cntf += 1
            if cnte - cntf >= 0:
                dp[i] = cnte - cntf
            else:
                dp[i] = 0
                cnte, cntf = 0, 0
        print(dp)
        print(max(dp))
    except EOFError:
        break

while True:
    try:
        n = int(input())
        s = input().split()
        ss = s[0]
        cnte, cntf = 0, 0
        maxx = 0
        for i in range(n):
            for j in range(i, n):
                cnte = ss[i:j+1].count('E')
                cntf = ss[i:j+1].count('F')
                maxx = max(maxx, cnte - cntf)
        print(maxx)
    except EOFError:
        break