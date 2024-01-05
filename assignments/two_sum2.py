class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map1={}
        for i, a in enumerate(numbers):
            b=target-a
            if b in map1:
                return [map1[b], i+1]
            map1[a]=i+1
