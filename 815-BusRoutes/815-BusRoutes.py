# Last updated: 6/19/2025, 9:49:30 PM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        bus_stops = {}
        # Construct Adjacency List
        # Key == route
        # Value == Index of route that contains this stop
        # {0:[1,2,3]} Means 0 index route has destinations 1 2 3
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in bus_stops:
                    bus_stops[stop] = []
                bus_stops[stop].append(i)
        
        visited = set()  # visited buses only
        queue = deque()

        if source not in bus_stops or target not in bus_stops:
            return -1 

        for bus in bus_stops[source]:
            queue.append((bus, 1))
            visited.add(bus)
        while queue:
            currBus, numBus = queue.popleft()

            for stop in routes[currBus]:
                if stop == target:
                    return numBus
                for connectedBus in bus_stops[stop]:
                    if connectedBus not in visited:
                        visited.add(connectedBus)
                        queue.append((connectedBus, numBus + 1))
        
        return -1