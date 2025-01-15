class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Depending on the position of the car, the time it takes for a car
        # at position i will determine whether to form a fleet or not
        time = [(target - position[i]) / speed[i] for i in range(len(speed))]
        # Sort in position, time
        stack = sorted(zip(position,time), reverse = True) # sort according to position, closest to target
        fleet = 0
        time = 0
        for p,t in stack:
            if time < t:
                fleet += 1
                time = t
        return fleet            



