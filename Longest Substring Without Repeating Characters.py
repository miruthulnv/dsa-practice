class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = len(s)
        sub =''
        out = 0
        i=0
        j=0
        out_L = []
        while (i<le):
            if(s[i] not in sub):
                sub+=s[i]
                out+=1
            else:
                j+=1
                i=j
                sub=s[i]
                out_L.append(out)
                out=1
            i+=1
        out_L.append(out)
        return max(out_L)
