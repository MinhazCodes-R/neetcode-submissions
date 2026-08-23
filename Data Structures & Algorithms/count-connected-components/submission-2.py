class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        seen_node = set()

        connections = 0


        adj_list = defaultdict(list)
        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        for i in range(n):
            if i not in adj_list:
                adj_list[i]

        def dfs(node,is_first):
            nonlocal connections
            nonlocal adj_list

            if node is None: return
            if node in seen_node: return

            if is_first: connections += 1

            seen_node.add(node)

            for neighbour_node in adj_list[node]:
                dfs(neighbour_node,False)

        for node,neighbour in adj_list.items():
            dfs(node,True)

        return connections 


        