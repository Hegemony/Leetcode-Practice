'''
滑动窗口:
思路：
这道题主要用到思路是：滑动窗口

什么是滑动窗口？

其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列变成了 abca，
这时候不满足要求。所以，我们要移动这个队列！

如何移动？

我们只要把队列的左边的元素移出就行了，直到满足题目要求！

一直维持这样的队列，找出队列出现最长的长度时候，求出解！

时间复杂度：O(n)O(n)

'''

def lengthOfLongestSubstring(s):
    if not s:
        return 0

    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0

    for i in range(n):
        cur_len += 1
        while s[i] in lookup:
            # 如果有重复两次的就把前面的都移走，直到集合里面没有重复的
            lookup.remove(s[left])
            left += 1
            cur_len -= 1

        if cur_len > max_len:
            max_len = cur_len

        lookup.add(s[i])
        print(lookup)
    print(max_len)
    return max_len

lengthOfLongestSubstring('abcdaamnytuaa')


"""
利用defaultdict(int)
"""
def lengthOfLongestSubstring1(s):
    """
    :type s: str
    :rtype: int
    """
    from collections import defaultdict
    lookup = defaultdict(int)
    start = 0
    end = 0
    max_len = 0
    counter = 0
    while end < len(s):
        if lookup[s[end]] > 0:
            counter += 1
        lookup[s[end]] += 1
        end += 1
        while counter > 0:
            if lookup[s[start]] > 1:
                counter -= 1
            lookup[s[start]] -= 1
            start += 1
        max_len = max(max_len, end - start)
        # print(max_len)
    return max_len

lengthOfLongestSubstring1('abcdaa')

