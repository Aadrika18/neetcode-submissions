class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def bkt(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False


            if board[i][j] != word[k]:
                return False

 
            temp = board[i][j]
            board[i][j] = "#"

          
            found = (
                bkt(i + 1, j, k + 1) or
                bkt(i - 1, j, k + 1) or
                bkt(i, j + 1, k + 1) or
                bkt(i, j - 1, k + 1)
            )

           
            board[i][j] = temp

            return found

      
        for i in range(rows):
            for j in range(cols):
                if bkt(i, j, 0):
                    return True

        return False