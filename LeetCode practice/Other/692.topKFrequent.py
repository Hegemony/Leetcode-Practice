class Solution:
    def topKFrequent(self, words, k: int):
        dic = {}
        for i in range(0, len(words)):
            dic[words[i]] = dic.get(words[i], 0) + 1
        res = []
        for i in dic.keys():
            res.append([i, dic[i]])
        res.sort(key=lambda x: (-x[1], x[0]))  # 次数升序，首字母降序
        result = []
        for i in range(k):
            result.append(res[i][0])
        return result


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
