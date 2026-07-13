class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        word_set = {c:set() for word in words for c in word}

        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            min_length = min(len(w1),len(w2))
            boolean = False
            for p in range(min_length):
                if w1[p] != w2[p]:
                    word_set[w1[p]].add(w2[p])
                    boolean = True
                    break
            if not boolean and len(w1)>len(w2):
                return ""
            

            

        comp_list,out_arr,visiting = set(),[],set()
        cycle = False
        def post_dfs(node):
            nonlocal cycle
            
            if (node in comp_list): return
            if (node in visiting): 
                cycle = True
                return
                
            else: visiting.add(node)

            for child in word_set[node]:
                post_dfs(child)

            visiting.remove(node)
            comp_list.add(node)
            out_arr.append(node)
            return 

        for node in word_set:
            post_dfs(node)

        if cycle: return ""
        out_arr.reverse()
        return_string = "".join(out_arr)

        return return_string

        