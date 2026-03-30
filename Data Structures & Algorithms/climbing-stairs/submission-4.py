class Solution:
    def climbStairs(self, n: int) -> int:
        climbing_dictionary = {}

        def climbAtI(i: int):
            if i == n or i == n - 1:
                return 1
            if i in climbing_dictionary:
                return climbing_dictionary[i]

            climbing_dictionary[i] = climbAtI(i + 1) + climbAtI(i + 2)
            return climbing_dictionary[i]
       
        return climbAtI(0)

