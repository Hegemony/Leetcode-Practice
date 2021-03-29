class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j] != ' ':
                if j == len(s) - 1:
                    res.append(s[i:j + 1])
                    break
                else:
                    j += 1
            else:
                res.append(s[i:j])
                while s[j] == ' ':
                    j += 1
                i = j
        res.reverse()
        return ' '.join(res)