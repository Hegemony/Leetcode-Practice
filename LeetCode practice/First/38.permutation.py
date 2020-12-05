class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        s = list(sorted(s))
        def helper(s, tmp):
            if not s:
                res.append(''.join(tmp))
            for i, char in enumerate(s):
                if i > 0 and s[i] == s[i - 1]:
                    continue
                helper(s[:i] + s[i+1:], tmp + [char])
                # tmp.append(char)
                # helper(s[:i] + s[i+1:], tmp)
                # tmp.pop()

        helper(s, [])
        return res

