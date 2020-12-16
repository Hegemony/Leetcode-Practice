class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            tmp = tuple(sorted(i))
            dic[tmp] = dic.get(tmp, []) + [i]
        res = []
        for i in dic:
            res.append(i)
        return res


i = 'bac'
tmp = tuple(sorted(i))
print(tmp)
