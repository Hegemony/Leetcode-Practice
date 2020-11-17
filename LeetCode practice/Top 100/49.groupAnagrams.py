"""
字典中：value可以取任何数据类型，但 key 必须是不可变的，如字符串，数字或元组。
用排序好的字符串，形成一个元组，作为key
"""
class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            key = tuple(sorted(i))
            dic[key] = dic.get(key, []) + [i]
        return list(dic.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

