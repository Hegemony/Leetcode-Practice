class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        tmp = []
        res = []

        def dfs(index):
            if index == len(digits):
                res.append(''.join(tmp))
            else:
                digit = digits[index]
                for i in dic[digit]:
                    tmp.append(i)
                    dfs(index + 1)
                    tmp.pop()

        dfs(0)
        return res
