class Solution:
    def reverseWords(self, s: str) -> str:
        # print(s.split(' '))
        return " ".join(word[::-1] for word in s.split(" "))