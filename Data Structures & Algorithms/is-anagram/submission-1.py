# initial thoughts: 
# iterate through each string and store the char frequency in separate 
# dictionaries and compare them using the equals operator to return True if they are equal
# and False if not equal

# time complexity: O(n)
# space complexity: O(n)

# optimization: combine s and t into one list and return 
# False if an index in the dictionary is > 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lst = list(s)
        sort = lst.sort()

        lst2 = list(t)
        sort2 = lst2.sort()

        if lst == lst2:
            return True
        else:
            return False


