"""
& 与  两个位都为1时，结果才为1     （统计奇数） 全1为1

| 或   两个位都为0时，结果才为0     (统计偶数） 全0为0

^ 异或    两个位相同为0，相异为1    (常用统计不相同数）  不同为1

~ 取反    0变1，1变0

<<  左移   各二进位全部左移若干位，高位丢弃，低位补0

>>  右移   各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移）
"""

"""
0x7fffffff 是最大的正数的补码 
0x80000000 是最小的负数的补码
"""
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x  # 处理成32位整型数
        print(b, b & x)

        while b != 0:
            a, b = (a ^ b), ((a & b) << 1) & x     # 非进位和，进位
        return a if a <= 0x7fffffff else ~ (a ^ x)
        # 若补码 aa 为负数（ 0x7fffffff 是最大的正数的补码 ），需执行 ~(a ^ x) 操作，将补码还原至 Python 的存储格式。
        # a ^ x 运算将 1 至 32 位按位取反； ~ 运算是将整个数字取反；因此， ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。



# print(Solution().add(2, -3))
print(bin(-3))
b = bin(-3 & 0xffffffff)
print(b)
c = bin(-3 ^ 0xffffffff)
print(c)
d = bin(~(-3 ^ 0xffffffff))
print(d)