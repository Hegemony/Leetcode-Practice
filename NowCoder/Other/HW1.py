while True:
    try:
        n = int(input())
        if n <= 0:
            x = ''
            print()
        elif n <= 1:
            x = 0
        elif n <= 3:
            x = 1
        elif n > 3:
            x = 0
            while n > 3:
                a = n // 3  # 换得的空瓶数
                b = n % 3
                n = a + b
                x += a  # 换得的汽水瓶数
            if n == 2 or n == 3:
                x = x + 1
        print(x)
    except EOFError:
        break