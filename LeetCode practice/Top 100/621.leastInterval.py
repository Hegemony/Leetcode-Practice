class Solution:
    def leastInterval(self, tasks, n) -> int:
        """
        https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
        :param tasks:
        :param n:
        :return:
        """
        l = len(tasks)
        if l <= 1:
            return l
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0) + 1
        max_value = 0
        for value in dic.values():
            max_value = max(max_value, value)
        count = 0
        for key in dic:
            if dic[key] == max_value:
                count += 1
        res = (max_value - 1) * (n + 1) + count

        return res if res > l else l

