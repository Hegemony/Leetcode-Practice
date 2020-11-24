class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dics = {}
        dict = {}
        for i in range(len(s)):
            dics[s[i]] = dics.get(s[i], 0) + 1
        for i in range(len(t)):
            dict[t[i]] = dict.get(t[i], 0) + 1

        return dics == dict