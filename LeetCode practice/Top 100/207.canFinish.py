class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        indegrees = [0 for i in range(numCourses)]
        # 统计课程安排图中每个节点的入度，生成 入度表 indegrees
        adjacency = [[] for i in range(numCourses)]
        # 通过课程前置条件列表 prerequisites 可以得到课程安排图的 邻接表 adjacency
        q = []  # 模拟队列
        for cur, pre in prerequisites:
            indegrees[cur] += 1  # 列表的索引对应每个课程，计算每个课程节点的入度,遇到课程结点，该课程的入度加1
            adjacency[pre].append(cur)  # 列表的索引对应每个课程，索引指向课程集合，索引即这些课程集合的前驱节点
        for i in range(len(indegrees)):
            if not indegrees[i]:  # 找到课程入度为0的所有节点
                q.append(i)
        while q:
            pre = q.pop(0)  # 删除课程结点
            numCourses -= 1
            for cur in adjacency[pre]:  # 找到该课程结点的指向的课程集合
                indegrees[cur] -= 1  # 课程集合中的每个课程的入度减1
                if not indegrees[cur]:  # 同时将减1后的入度结点为0的课程加入到队列中
                    q.append(cur)
        return not numCourses


prerequsistes = [[1, 0], [0, 1]]
indegrees = [0 for i in range(2)]
# 统计课程安排图中每个节点的入度，生成 入度表 indegrees
adjacency = [[] for i in range(2)]
for cur, pre in prerequsistes:
    print(cur, pre)
    indegrees[cur] += 1
    adjacency[pre].append(cur)
print(indegrees)
print(adjacency)
