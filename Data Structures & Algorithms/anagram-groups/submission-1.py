# approach: create a dictionary, sort with string, store that
# as the key in the dictionary, append the string to this list
# of the key. 
# return the values as a list
# time complexity: O(n * m log m), where n is the length of the hashmap and m is the length of each key's list and log m is the sorting of each string we iterate over
# space complexity: O(n * m) as hashmap can grow over n strings and up to length m for each key in the map that is an anagram
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            key = "".join(sorted(s))
            if key not in d:
                d[key] = []
            d[key].append(s)
            
        return list(d.values())