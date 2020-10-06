def isValid(s):
    n = len(s)
    if n == 0:
        return True
    if n % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    res = []
    for i in s:
        if i in pairs.values():  # 左括号进栈
            res.append(i)
        elif i in pairs:   # 右括号出栈比较
            if len(res) == 0:   # 第一个符号为右括号
                return False
            if res.pop() != pairs[i]:
                return False

    return res == []
print(isValid("){"))

# pairs = {
#         ")": "(",
#         "]": "[",
#         "}": '{'
#     }
# stack = []
# for i in pairs:  # 遍历字典
#     print(i)
#     print(pairs[i])
