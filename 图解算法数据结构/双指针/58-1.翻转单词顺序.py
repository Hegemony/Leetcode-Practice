class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = len(s)
        i, j = 0, 0
        result = []
        while j < l:
            while j < l and s[j] != ' ':
                j += 1
            result.append(s[i:j])

            while j < l and s[j] == ' ':
                j += 1
            i = j
        result.reverse()
        return ' '.join(result)


print(Solution().reverseWords("the sky is blue"))
