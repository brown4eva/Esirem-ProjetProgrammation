class Board:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.clear()

    def clear(self):
        # Create a 2D array (list of lists) filled with '.' to represent a clear board
        self.board = [['.' for _ in range(self.columns)] for _ in range(self.rows)]

    def __repr__(self):
        # Create a string representation of the board
        board_str = ''
        for row in self.board:
            board_str += '|' + ''.join(row) + '|\n'
        return board_str

    

# Initialize the Board instance, creating a mimic of Puissance 4
board = Board(5, 7)  # 5 rows and 7 columns 

# Manually place some tokens on the board, J => jaune, R => Rouge
board.board[1][2] = 'J'  
board.board[2][1] = 'R'
board.board[2][4] = 'J'
board.board[3][4] = 'R'
board.board[4][4] = 'J'

# Print the board
print(board)
