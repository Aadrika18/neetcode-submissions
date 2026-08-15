class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def palindrome(ch):
            return ch == ch[::-1]

        def bkt(start):
            if start == len(s):
                res.append(curr.copy())
                return

            for end in range(start + 1, len(s) + 1):
                ch = s[start:end]

                if palindrome(ch):
                    curr.append(ch)
                    bkt(end)
                    curr.pop()

        bkt(0)
        return res
                
        
       


        