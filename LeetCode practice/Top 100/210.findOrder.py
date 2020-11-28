class Solution:
    def findOrder(self, numCourses, prerequisites):
        l = numCourses
        indegrees = [0 for i in range(numCourses)]
        adjacency = [[] for i in range(numCourses)]
        q = []
        res = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
                res.append(i)
                print('*', res)
        while q:
            pre = q.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    q.append(cur)
                    res.append(cur)
                    print(res)
        return res if len(res) == l else []


print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
