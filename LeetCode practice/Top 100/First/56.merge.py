class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        merged.append(intervals[0])
        for i in intervals:
            if merged[-1][1] >= i[0]:
                merged[-1][1] = max(i[1], merged[-1][1])
            else:
                merged.append(i)
        return merged