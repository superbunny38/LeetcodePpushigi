class Solution:
    def reverseVowels(self, s):
        if len(s) == 1:
            return s
        l,r = 0, len(s)-1
        vowels = set(['a','e','i','o','u'])
        s=list(s)
        while l<r:
            if s[l].lower() not in vowels:
                l+=1
                
            if s[r].lower() not in vowels:
                r-=1
            
            if s[l].lower() in vowels and s[r].lower() in vowels:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1

        return "".join(s)

ans = Solution().reverseVowels(s="IceCreAm")
print(ans)