class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board:
            return
        
        m = len(board)
        n = len(board[0])
        
        if m <= 1 or n <= 1:
            return
        
        # table recording whether a location has been visited
        visited = [[False for i in range(n)] for j in range(m)] 
        
        # queue containing all boundary "O"
        queue = []
        # first col
        j = 0
        for i in range(m):
            if board[i][j] == 'O':
                visited[i][j] = True
                queue.append((i,j))
        # last col
        j = n - 1
        for i in range(m):
            if board[i][j] == 'O':
                visited[i][j] = True
                queue.append((i,j))
        # first row
        i = 0
        for j in range(n):
            if board[i][j] == 'O':
                visited[i][j] = True
                queue.append((i,j))
        # last row
        i = m - 1
        for j in range(n):
            if board[i][j] == 'O':
                visited[i][j] = True
                queue.append((i,j))
        
        # DFS for all "O" and replace them with "#"
        while queue:
            i, j = queue.pop()
            board[i][j] = '#'
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and visited[x][y] == False:
                    visited[x][y] = True
                    queue.append((x,y))
        
        # final scan, replacing "O" with "X" and "#" with "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'