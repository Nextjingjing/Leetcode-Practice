class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for mainIndex in range(len(s)):
            unrepeatedString = ""
            for index in range(mainIndex, len(s)):
                char = s[index]
                if index == mainIndex:
                    unrepeatedString += char
                elif unrepeatedString.find(char) == -1:
                    unrepeatedString += char        
                else:
                    break
                
            if len(unrepeatedString) > maxLen:
                maxLen = len(unrepeatedString)
        
        return maxLen