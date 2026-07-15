class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #pretty generic bfs style of question
        '''

        idea is we do a bfs search starting at a treasure chest
        so we will need a visited set
        
        then the idea is we start our queue with the treasure chest
        and continue to pop the queue and process the values until the queue is empty

        if we encounter a water cell then we continue (dont process)
        or if we encounter a cell that we already visisted

        if its a land cell then we do this:
            we set the value in the array to the distance value we have
        add everything to the left,right,up,down
        so as we compute we should add (x,y,distance) to the queue where distance
        when we process we will take the distance+1 and add it alongside 
        (x+1,y), (x-1,y), (x,y+1), (x,y-1)

        is the distance to the treasure and we will make sure to continue to
        increment this accordingly

        example:
        xxxxxxx
        xxxxxxx
        xx0xxxx
        xxxxxxx
        '''

        visited,queue = set(), deque()
        #queue.pop() and queue.append()
        for row,arr in enumerate(grid):
            for column,val in enumerate(arr):
                if val == 0: 
                    queue.append((0,column,row))


        while queue:
            distance,x,y = queue.popleft()
            #bounds
            if (x<0) or x>len(grid[0])-1 or y<0 or y>len(grid)-1: continue

            if (x,y) in visited or grid[y][x] == -1: continue

            if grid[y][x] != 0: grid[y][x] = min(distance,grid[y][x])
            visited.add((x,y))

            queue.append((distance+1,x+1,y))
            queue.append((distance+1,x-1,y))
            queue.append((distance+1,x,y+1))
            queue.append((distance+1,x,y-1))




        