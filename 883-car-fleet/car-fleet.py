class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # A car fleet travels at the minimum speed of any car in the fleet
        time = [(target - position[i]) / speed[i] for i in range(len(speed))]
        cars = sorted(zip(position, time), reverse = True) # sort using position
        # first element in time will be the shortest time
        fleet = 0
        cur_time = 0
        for _, t in cars:
            if t > cur_time: # Not a fleet
                fleet += 1
                cur_time = t
        return fleet        
            