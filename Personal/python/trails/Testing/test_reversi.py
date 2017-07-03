# This function prints out the board that it was passed. Returns None.

board = []
for i in range(8):
    board.append([' '] * 8)

for x in range(8):
    for y in range(8):
        board[x][y] = ' '


HLINE = '  +---+---+---+---+---+---+---+---+'
VLINE = '  |   |   |   |   |   |   |   |   |'

print('    1   2   3   4   5   6   7   8')
print(HLINE)
for y in range(8):
    print(VLINE)
    print(y+1, ' ')
    for x in range(8):
        print('| %s' % (board[x][y]), ' ')
    print('|')
    print(VLINE)
    print(HLINE)