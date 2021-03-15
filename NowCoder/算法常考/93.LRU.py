#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
class Solution:
    def LRU(self, operators, k):
        # write code here
        stack = []
        kv_pair = {}
        ans = []
        for op in operators:
            if op[0] == 1:
                if len(stack) < k:
                    stack.append((op[1], op[2]))
                    kv_pair[op[1]] = op[2]
                else:
                    key, value = stack.pop(0)
                    kv_pair.pop(key)
                    stack.append((op[1], op[2]))
                    kv_pair[op[1]] = op[2]
            elif op[0] == 2:
                if op[1] not in kv_pair:
                    ans.append(-1)
                else:
                    record = kv_pair[op[1]]
                    ans.append(record)
                    stack.remove((op[1], kv_pair[op[1]]))
                    stack.append((op[1], record))
        return ans
