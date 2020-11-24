class Solution:
    def findMinArrowShots(self, points) -> int:
        if len(points) == 0:
            return 0
        cur, res = points[0][1], 1
        points.sort(key=lambda x: x[0])
        for i in range(len(points)):
            if cur >= points[i][0]:
                cur = min(points[i][1], cur)
            else:
                cur = points[i][1]
                res += 1
        return res


# a = [1, 2, 3, 4, 5, 6]
# s = a[:]
# for i in range(len(s)):
#     a.remove(s[i])
#     print(a)
