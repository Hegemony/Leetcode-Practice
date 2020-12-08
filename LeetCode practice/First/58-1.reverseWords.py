class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i, j = 0, 0
        res = []
        while j < len(s):
            while j < len(s) and s[j] != ' ':   # j 要小于len(s), 因为下面的while产生的j+1可能会超出索引
                j += 1
            res.append(s[i:j])
            while j < len(s) and s[j] == ' ':  # j 要小于len(s), 因为上面面的while产生的j+1可能会超出索引
                j += 1
            i = j
        res.reverse()
        return ' '.join(res)


print(Solution().reverseWords("the sky is blue"))
