"""
(1) strip()方法语法：

str.strip([chars]);
参数
chars -- 移除字符串头尾指定的字符序列。

s = s.strip()  # 删除首尾空格 要赋值给新的列表


(2) join()方法语法：

str.join(sequence)
参数
sequence -- 要连接的元素序列。
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
r-u-n-o-o-b
runoob
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        print(s.strip())
        i = 0
        j = 0
        n = len(s)
        res = []
        while j < n:
            while j < n and s[j] != ' ':  # 搜索首个空格
                j += 1
            res.append(s[i:j])  # 添加单词
            print(res)
            while j < n and s[j] == ' ':  # 跳过单词间空格
                j += 1
            i = j  # i 指向下个单词的首字符
        res.reverse()
        print(res)
        return ' '.join(res)  # 拼接并返回

print(Solution().reverseWords("  hello world!  "))
print(len(Solution().reverseWords("  hello world!  ")))
# s1 = " "
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b")  # 字符串序列
# print(s1.join(seq))
# print(len(s1.join(seq)))
# print(s2.join(seq))
