class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort in dict:
                dict[sort].append(s)
            else:
                dict[sort] = [s]
        return list(dict.values())
            