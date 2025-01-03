class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We'll use a hashmap to store the values
        # And then we'll check whether the current number + 1 (-1 approach results in multiple search that is no good I guess?)
        # exists inside the hashmap. We'll iterate our count integer when such number exists, and keep track of the biggest number so far. Time complexity will be O(n) as we loop through the array once, and look up in hashmap is O(1) so overall time complexity will be O(n)
        # space complexity will be O(n) for the hashmap that we use
        # 
        if len(nums) == 0:
            return 0
        numsMap = set(nums)
        maximum = 1
        for n in numsMap:
            # start the sequence with the smallest number
            if n - 1 in numsMap:
                continue
            else:
                cur = 1
                while n + 1 in numsMap:
                    cur += 1
                    n += 1
                maximum = max(maximum, cur)     
        return maximum       