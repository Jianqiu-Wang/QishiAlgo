"""
Description
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
Problem Correction
Example

Input: n = 2, 
Output: ["11","69","88","96"]
Example 2:

Input: n = 1, 
Output: ["0","1","8"]
"""
class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        def my_strobogrammatic(n):
            if n == 1: return ["0","1","8"]
            if n == 2: return ["00", "11","69","88","96"]
            temp = []
            if n % 2 == 0:
                str_list1 = my_strobogrammatic(n-2)
                for x in str_list1:
                    temp += [x[:(n/2-1)]+y+x[n/2-1:] for y in ["00","11","88", "69","96"]]
    
            else:
                str_list1 = my_strobogrammatic(n-1)
                for x in str_list1:
                    temp += [x[:(n/2)]+y+x[n/2:] for y in ["0","1","8"]]
            return temp
        
        if n == 0: return [""]
        elif n == 1: return ["0","1","8"]
        else:
            res = my_strobogrammatic(n)
            res = [x for x in res if x[0] != "0"]
            return res