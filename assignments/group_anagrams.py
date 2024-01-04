class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramgroup = defaultdict(list)
        for i in strs:
            isorted = ''.join(sorted(i))
            anagramgroup[isorted].append(i)
        return list(anagramgroup.values())
