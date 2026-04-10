
class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag1 = 0
        self.diag2 = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        curr_player = 1 if player == 1 else -1

        self.rows[row] += curr_player
        self.cols[col] += curr_player

        if row == col:
            self.diag1 += curr_player
        if row + col == self.n - 1:
            self.diag2 += curr_player

        # win
        win_criteria = self.n * curr_player
        if self.rows[row] == win_criteria or self.cols[col] == win_criteria or self.diag1 == win_criteria or self.diag2 == win_criteria:
            return player
        return 0

Instead of storing a grid, the class tracks:
rows[i] → sum of a row
cols[j] → sum of a column
diag1 → main diagonal
diag2 → anti-diagonal
Player 1 = +1
Player 2 = -1

A player wins when the sum becomes:
+ n  → Player 1 wins
- n  → Player 2 wins

Instead of checking the whole board:

Traditional approach:
Scan row → O(n)
Scan column → O(n)
Scan diagonals → O(n)
This approach:
Just update counters → O(1)
Each row/col/diagonal acts like a score counter
If one player fully occupies it → sum becomes ±n

if __name__ == "__main__":
    tic_tac_toe = TicTacToe(3)
    print(tic_tac_toe.move(0, 0, 1))  # Player 1 moves at (0, 0) → Output: 0 (no winner)
    print(tic_tac_toe.move(0, 2, 2))  # Player 2 moves at (0, 2) → Output: 0 (no winner)
    print(tic_tac_toe.move(2, 2, 1))  # Player 1 moves at (2, 2) → Output: 0 (no winner)
    print(tic_tac_toe.move(1, 1, 2))  # Player 2 moves at (1, 1) → Output: 0 (no winner)
    print(tic_tac_toe.move(2, 0, 1))  # Player 1 moves at (2, 0) → Output: 0 (no winner)
    print(tic_tac_toe.move(1, 0, 2))  # Player 2 moves at (1, 0) → Output: 0 (no winner)
    print(tic_tac_toe.move(2, 1, 1))  # Player 1 moves at (2, 1) → Output: 1 (Player 1 wins)