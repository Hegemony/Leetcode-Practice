class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            tmp = tuple(sorted(i))
            dic[tmp] = dic.get(tmp, []) + [i]
        res =[]
        for i in dic:
            res.append(dic[i])
        return res


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
