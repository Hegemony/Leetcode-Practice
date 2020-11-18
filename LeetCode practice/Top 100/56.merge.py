"""
1、内置函数sort（）

原型：sort（fun，key，reverse=False）
参数fun是表明此sort函数是基于何种算法进行排序的，一般默认情况下python中用的是归并排序，并且一般情况下我们是不会重写此参数的，所以基本可以忽略；
参数key用来指定一个函数，此函数在每次元素比较时被调用，此函数代表排序的规则，也就是你按照什么规则对你的序列进行排序；
参数reverse是用来表明是否逆序，默认的False情况下是按照升序的规则进行排序的，当reverse=True时，便会按照降序进行排序。
"""


class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])   # 按照第一个关键字进行排序
        merged = []
        if len(intervals) == 0:
            return merged
        merged.append(intervals[0])
        for i in intervals:
            if merged[-1][1] >= i[0]:         # 如果merged区间的右侧大于等于intervals区间的左侧，就合并区间，更新merged区间右侧
                merged[-1][1] = max(i[1], merged[-1][1])
            else:                            # 如果merged区间的右侧小于intervals区间的左侧，则不可以合并区间，将该区间添加到merged
                merged.append(i)
        return merged


print(Solution().merge([[1, 4], [4, 5]]))
