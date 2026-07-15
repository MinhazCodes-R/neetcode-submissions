class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def a_exists_in_b(a_map,b_map):
            for key,value in a_map.items():
                if value > b_map.get(key,0): return False

            return True

        smallest_string = float('inf')
        return_str = ""
        our_window ={s[0]:1}
        t_window = {}
        for character in t: t_window[character] = t_window.get(character,0) + 1
        lp,rp = 0,0
        while lp<len(s):
            if a_exists_in_b(t_window,our_window):
                if smallest_string>rp-lp+1:
                    smallest_string = rp-lp+1
                    return_str = s[lp:rp+1]
                our_window[s[lp]] = our_window[s[lp]] - 1 
                lp += 1
            elif (rp<len(s)-1):
                our_window[s[rp+1]] = our_window.get(s[rp+1],0) + 1
                rp += 1
            else:
                break
        return return_str

                



        