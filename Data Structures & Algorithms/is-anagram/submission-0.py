# initial thoughts: 
# iterate through each string and store the char frequency in separate 
# dictionaries and compare them using the equals operator to return True if they are equal
# and False if not equal

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}

        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
        
        for c in t:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1

        if d1 == d2:
            return True
        else:
            return False