# Last updated: 6/20/2025, 10:36:28 PM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        visited_routes = set()
        visited_stops = set([source])
        queue = deque()

        for route in stop_to_routes[source]:
            queue.append((route, 1))
            visited_routes.add(route)
        
        while queue:
            current_route, buses_taken = queue.popleft()
            
            if target in routes[current_route]:
                return buses_taken
            
            for stop in routes[current_route]:
                if stop not in visited_stops:
                    visited_stops.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            queue.append((next_route, buses_taken + 1))
                            visited_routes.add(next_route)
        
        return -1
