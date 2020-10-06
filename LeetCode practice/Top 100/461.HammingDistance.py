"""
python之间的进制转换
(1)转化成二进制：
a = 10  #声明数字，默认十进制
b = bin(a)  # 得到的是字符串，可以用int(b, base= )转换为int类型

(2)转换为八进制：
a = 10  #声明数字，默认十进制
b = oct(a)

(3)转换为十六进制：
a = 10  #声明数字，默认十进制
b = hex(a)
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# a = 10  #声明数字，默认十进制
# b = bin(a)  # 得到的是字符串，可以用int()转换为int类型
# print(b, type(b))
# print(int(b, base=2))
