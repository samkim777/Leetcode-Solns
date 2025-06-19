# Last updated: 6/18/2025, 11:14:50 PM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        bus_stops = {}
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in bus_stops:
                    bus_stops[stop] = []
                bus_stops[stop].append(i)
        
        visited = set()  # visited buses only
        queue = deque()

        for bus in bus_stops.get(source, []):
            queue.append((bus, 1))
            visited.add(bus)
        
        while queue:
            currBus, numBus = queue.popleft()

            for stop in routes[currBus]:
                if stop == target:
                    return numBus
                for connectedBus in bus_stops.get(stop, []):
                    if connectedBus not in visited:
                        visited.add(connectedBus)
                        queue.append((connectedBus, numBus + 1))
        
        return -1