class Solution:
    def checkValidString(self, s: str) -> bool:
        #we read left to right and treat ( and * as the same
        # add 1 if they exist otherwise subtract 1
        #idea is if we treat all the stars as ( will we be able to match enough 
        #each of the ( with the corresponding )

        #do the same thing right to left
        #and the idea is that if we treat all the * as ) can we match it
        #if at any point we cant match it it is invalid

        balance = 0
        for character in s:
            balance += 1 if character in "(*" else -1
            if balance<0: return False
        balance = 0
        for character in reversed(s):
            balance += 1 if character in ")*" else -1
            if balance<0: return False

        return True

       