import random

SIZE = 9
MINES = 10

FLAG= "F"
HIDDEN= "-"
MINE= "*"

def create_board():
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    mine_positions = set()
    while len(mine_positions) < 10:
        r, c = random.randint(0,SIZE-1), random.randint(0,SIZE-1)
        if (r, c) not in mine_positions:
            mine_positions.add((r, c))
            board[r][c] = MINE
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and board[nr][nc] != MINE:
                        board[nr][nc] += 1
    return board, mine_positions

def print_board(visible, flags):
    print("   "+" ".join(map(str, range(SIZE))))
    for r in range(SIZE):
        row = []
        for c in range(SIZE):
            if(r,c) in flags:
                row.append(FLAG)
            elif visible[r][c]:
                val = actual_board[r][c]
                row.append(str(val) if val != 0 else " ")
            else:
                row.append(HIDDEN)
        print(f"{r:2} {' '.join(row)}")

def reveal(r, c, visible):
    if not(0 <= r < SIZE and 0 <= c < SIZE) or visible[r][c]:
        return
    visible[r][c]=True
    if actual_board[r][c] == 0:
        for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr != 0 or dc != 0:
                        reveal(r+dr, c+dc, visible)

actual_board, mine_positions = create_board()
visible = [[False for _ in range(SIZE)] for _ in range(SIZE)]
flags = set()

while True:
    print_board(visible, flags)
    move = input("Enter move (r row col / f row col): ").split()
    print(f"Flags: {len(flags)+1}")
    if len(move) != 3:
        print("Invalid Input!!")
        continue
    action, row, col = move[0], int(move[1]), int(move[2])
    if not(0 <= row < SIZE and 0 <= col < SIZE):
        print("Out of Bounds!!")
        continue
    if action == "f":
        if (row, col) in flags:
            flags.remove((row, col))
        else:
            flags.add((row, col))
    elif action == "r":
        if (row, col) in mine_positions:
            print_board([[True]*SIZE for _ in range(SIZE)], flags)
            print("💥 BOOM! You hit a mine. Game over.")
            break
        reveal(row, col, visible)
        revealed_count = sum(visible[r][c] for r in range(SIZE) for c in range(SIZE))
        if revealed_count == SIZE*SIZE - 10:
            print_board(visible, flags)
            print("🎉 Congratulations! You cleared the board.")
            break
    else:
        print("Unknown action. Use 'r' to reveal or 'f' to flag.")