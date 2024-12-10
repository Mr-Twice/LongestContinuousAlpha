class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        substring_count = {}
    
        for length in range(1, n + 1):  # Length of the substring
            for i in range(n - length + 1):  # Start index
                substring = s[i:i + length]
                if len(set(substring)) == 1:  # Check if it's special
                    substring_count[substring] = substring_count.get(substring, 0) + 1
    
        max_length = -1
        for substring, count in substring_count.items():
            if count >= 3:
                max_length = max(max_length, len(substring))
    
        return max_length
