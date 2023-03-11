class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # Traverse twice as fast
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow] # Slow pointer starts at the first intersection
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2        
                     