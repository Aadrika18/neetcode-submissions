class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        if n is None:
            return []
        op = "("
        cl = ")"
        c_op  = 0
        c_cl = 0

     
        def bkt(c_op, c_cl):
            if c_op == c_cl == n:
                res.append("".join(stack))
                return

            if c_op < n:

                stack.append(op)
                bkt(c_op + 1, c_cl)
                stack.pop()
            if c_cl < c_op:
                stack.append(cl)
                bkt(c_op, c_cl + 1)
                stack.pop()
        
        bkt(c_op,c_cl)
        return res

                

        

        