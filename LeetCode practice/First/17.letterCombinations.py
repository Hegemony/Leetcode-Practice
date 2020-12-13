class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if len(digits) == 1:
            return [i for i in digit2chars[digits[0]]]
        res = [i for i in digit2chars[digits[0]]]
        result = []
        for i in digits[1:]:
            result = []
            print('*', res)
            for m in res:
                for n in digit2chars[i]:
                    result.append(m + n)
                res = result
                print(m, res)
        return result


# print(Solution().letterCombinations('234'))


class Solution1:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(index):
            if index == len(digits):
                res.append(''.join(tmp))
            else:
                digit = digits[index]
                for i in phoneMap[digit]:
                    tmp.append(i)
                    dfs(index + 1)
                    tmp.pop()

        tmp = []
        res = []
        dfs(0)
        return res


print(Solution1().letterCombinations('234'))

