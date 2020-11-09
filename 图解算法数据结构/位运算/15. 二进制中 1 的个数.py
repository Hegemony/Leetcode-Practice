class Solution:
    def hammingWeight(self, n: int) -> int:
        res = bin(n)
        return res.count('1')


"""
>> 和 <<都是位bai运算，对二进制数进行移位操作。
<< 是左移，末位补0，类比十进制数在末尾添0相当于原数乘以10，x<<1是将x的二进制表示左移一位，相当于原数x乘2。比如整数4在二进制下是100，
4 << 1左移1位变成1000(二进制)，结果是8。

>>是右移，右移1位相当于除以2。
而>>=和<<=，就是对变量进行位运算移位之后的结果再赋值给原来的变量，可以类比赋值运算符+=和-=可以理解。
比如x >>= 2， 就是把变量x右移2位，再保留x操作后的值。
"""
class Solution1:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            print(n, bin(n))
            res += n & 1
            n >>= 1
        return res

print(bin(20))
print(Solution1().hammingWeight(20))