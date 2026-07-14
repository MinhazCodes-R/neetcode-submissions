class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        djistras 
        we process the smallest element in a min_heap
        the elements will be tuples (price,stops,next_node)
        note that while we process if we notice that
        stops is more than k we will either set the price to infinity and append
        or we will just not process it at all (and not reintroduce it the minheap)
        '''
        min_heap,all_nodes,visited = [], set(), set()
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (0,-1,src))
        '''
        minheap with values of (price,level,node)
        once we pop an element we explore that elements neighbors
        add price to current price, +1 to the level and then add it back to the heap
        '''
        least_price = -1
        mapping = collections.defaultdict(list)
        '''
        node1 -> [(neighbour1,price1),(neighbour2,price2),(neighbour3,price3)]
        '''
        for from_i,to_i,price_i in flights:
            all_nodes.add(from_i)
            all_nodes.add(to_i)
            mapping[from_i].append((to_i,price_i))

        dist = {}

        while min_heap:
            #pop our element
            price,level,node = heapq.heappop(min_heap)
            if level > k or price >= dist.get((node, level), float('inf')): continue
            dist[(node, level)] = price

            if node == dst:
                return price

            neighbours = mapping[node]
            for node1,price1 in neighbours:
                heapq.heappush(min_heap,(price1+price,level+1,node1))

        return least_price