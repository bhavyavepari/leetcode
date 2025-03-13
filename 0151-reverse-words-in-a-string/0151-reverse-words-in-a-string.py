class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l=l[::-1]
        m=" ".join(l)
        return m