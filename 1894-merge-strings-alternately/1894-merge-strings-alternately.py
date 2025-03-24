class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=[]
        l1=len(word1)
        l2=len(word2)
        l=min(l1,l2)
    
        for i in range(l):
            a.append(word1[i])
            a.append(word2[i])
        a.extend(word1[l:]+word2[l:])
        b="".join(a)
        return b
            