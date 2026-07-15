class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Idea is that you pick a point
        and describe the cost to go from that point to every other point
        and then continiously discover the one with the lower cost
        and keep doing so until you visited all the point
        '''

        min_heap,visited,all_cords = [], set(), set()
        heapq.heapify(min_heap)

        adc_list = {}
        '''
        (cordx,cordy) -> [[(cordx1,cordy2),distance],[],[]]

        min_heap
        (distance,cordx,cordy)
        '''


        for index,(cordx,cordy) in enumerate(points):
            all_cords.add((cordx,cordy))
            for index1,(cordx1,cordy1) in enumerate(points):
                if index == index1: continue
                distance = abs(cordx-cordx1) + abs(cordy-cordy1)
                if (cordx,cordy) in adc_list:
                    adc_list[(cordx,cordy)].append((cordx1,cordy1,distance))
                else:
                    adc_list[(cordx,cordy)] = [(cordx1,cordy1,distance)]

        startx,starty = points[0]
        heapq.heappush(min_heap,(0,startx,starty))
        total_distance = 0

        while (visited != all_cords):
            distance,cordx,cordy = heapq.heappop(min_heap)
            if (cordx,cordy) in visited: continue
            total_distance += distance
            visited.add((cordx,cordy))
            nieghbours = adc_list.get((cordx,cordy))
            if not nieghbours : continue
            for cordx_n,cordy_n,distance in nieghbours:
                heapq.heappush(min_heap,(distance,cordx_n,cordy_n))
        return total_distance




                

        
        