class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        s_inv = s[::-1]  # s inverse
        max_len = 0
        temp_val = ""
        if n == 1 or n == 0:
            return s
        # Find longset common string between s and s_inv
        for i in range(n):
            if max_len <= n-i+1:
                for j in range(max_len, n-i+1):
                    if s[i:i + j] == s_inv[n-i-j:n-i]:
                        temp_val = s[i:i + j]
                        max_len = j 

        return temp_val