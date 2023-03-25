class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Guards will be back in h hours
        # Banana eating speed of k
        # Choose some pile, eats k from that pile
        # If i < k, she stays on that pile and eats no more for that hour
        # Return the minimum integer k s.t she can eat all the bananas
        # within h hours
        #
        # Note that h cannot be less than the amount of piles of banana
        # upper bound of k, then try to find the lower bound
        # upper k is maximum pile in the list
        # lower k is what we want to find
        # take upper k / 2, take that as the lower bound
        # We check if the lower bound speed gives us apporpriate h
        # For example, if given h is 6, and upper bound was k = 4,
        # and k = 2 let's say
        # Then, we need to increase the speed, so we will take the mid pt
        # between the upper bound k = 4 + k = 2 and divide by 2
        # We will continue until pointers l,r are equal
        upk = max(piles) # Upper k value
        lowk = 1
        res = upk
        while (lowk <= upk):
            midk = (upk + lowk) // 2 
            sum = 0
            for p in piles:
                sum += math.ceil(p / midk) # Using math.ceil
            if sum <= h:
                res = min(res,midk) # Key: taking the min of cur k speed
                upk = midk - 1
            else: 
                lowk = midk + 1    
        return res    



