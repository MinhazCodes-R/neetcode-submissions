class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0: return True
        all_nodes = set()
        for i in range(n): all_nodes.add(i)

        visited = set()
        adj_list = {}

        #to make the adj_list
        for (node1,node2) in edges:

            adj_list.setdefault(node1,[]).append(node2)
            adj_list.setdefault(node2,[]).append(node1)

        fail_ = False

        def dfs(node,prev_node):
            nonlocal visited
            nonlocal adj_list, fail_

            #checking for cycles
            if fail_ or node in visited:
                fail_ = True
                return

            #adding to visited
            visited.add(node)

            for neighbour in adj_list[node]:
                if neighbour != prev_node: dfs(neighbour,node)
                else: continue


        dfs(0,None)

        if fail_: return False
        if visited == all_nodes: return True
        return False




        