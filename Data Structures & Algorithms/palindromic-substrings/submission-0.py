class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindrom(start,end):
            count = 0
            #start=end
            while (start>=0 and end<len(s) and s[start] == s[end]):
                #process

                count += 1
                start -= 1
                end += 1

            return count

        #so now we just call this palindrom function twice
        #once with the same index (twice) and once with index, index + 1
        total_count = 0

        for index_val in range(0,len(s)):
            total_count += palindrom(index_val,index_val)
            total_count += palindrom(index_val,index_val+1)

        return total_count

        