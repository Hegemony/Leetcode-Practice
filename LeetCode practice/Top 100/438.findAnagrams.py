"""
暴力：解决6%
"""


class Solution:
    def findAnagrams(self, s, p):
        res = []
        p1 = sorted(list(p))
        step = len(p1)
        l = len(s)
        for i in range(0, l - step + 1):
            tmp = sorted(list(s[i:i + step]))
            if tmp == p1:
                res.append(i)
        return res


"""
利用字典的方法：
首先建立非空字符串p的comparator，记录字母出现的次数；
其次建立非空字符串s中前len(p)个字符的temp_dict，记录字母出现的次数；
进入滑动窗口循环：
1). 判断comparator与temp_dict是否相同，相同的话在res中存入当前字符串左边界的索引;
2). 滑动窗口右移：弹出字符串左边界的字符，相应的temp_dict中减去这个字符的次数；放入位于字符串右边界的右边的字符，
    在temp_dict中增加这个字符的次数；循环结束，输出res
"""


class Solution1:
    def findAnagrams(self, s: str, p: str):
        '''
        滑动窗口 + 哈希
        '''
        res = []
        window = {}  # 记录窗口中各个字符数量的字典
        dic = {}  # 记录目标字符串中各个字符数量的字典
        for i in p:
            dic[i] = dic.get(i, 0) + 1  # 统计目标字符串的信息
        left, right = 0, 0  # 定义两个指针，分别表示窗口的左、右界限
        len_s, len_p = len(s), len(p)
        while right < len_s:
            tmp = s[right]
            if tmp not in dic:  # 当遇到不需要的字符时
                window.clear()  # 将之前统计的信息全部放弃
                left, right = right + 1, right + 1  # 从下一位置开始重新统计
            else:
                window[tmp] = window.get(tmp, 0) + 1  # 统计窗口内各种字符出现的次数
                if right - left + 1 == len_p:  # 当窗口大小与目标字符串长度一致时
                    if window == dic:
                        res.append(left)  # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1  # 并将移除的字符数量减1
                    left += 1  # left右移
                right += 1  # right右移
                print(left, right)
        return res


print(Solution1().findAnagrams("cbaebabacd", "abc"))
