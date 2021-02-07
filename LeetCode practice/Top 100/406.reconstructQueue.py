class Solution:
    def reconstructQueue(self, people):
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))  # 先按照x[0]逆序排序，再按照X[1]正序排序
        for p in people:
            if len(res) <= p[1]:  # 尽量把高的排在前面
                res.append(p)
            elif len(res) > p[1]:
                res.insert(p[1], p)
        return res
