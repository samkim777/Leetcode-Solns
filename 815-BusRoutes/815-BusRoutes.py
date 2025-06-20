# Last updated: 6/19/2025, 10:15:48 PM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # create adjacency list
        bus_stops = defaultdict(list)
        for index, route in enumerate(routes):
            for stop in route:
                bus_stops[stop].append(index) # {route1: index of route array that contains route 1, 
            # route2: index of route array that contains route 2...}

        # Edge case for when our source or target is not inside any routes
        if source not in bus_stops or target not in bus_stops:
            return -1
        queue = deque()
        visited = set()

        # Start off queue from source --> We know source is in our routes
        for bus in bus_stops[source]:
            queue.append((bus,1))
            visited.add(bus)

        while queue:
            curidx, curBusNums = queue.popleft() # ex: 1, 3: index of route 1, 3 buses req

            for route in routes[curidx]:
                if route == target:
                    return curBusNums
                for connectedBus in bus_stops[route]:
                    if connectedBus not in visited:
                        queue.append((connectedBus, curBusNums + 1))
                        visited.add(connectedBus)
        return -1
