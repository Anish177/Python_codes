n = int(input('Size of the board: '))

board = [["-"] * n for i in range(n)]

print('Board without queens is:', *board, sep='\n\n', end='\n\n')

col = set()
diag1 = set() #(r + c)
diag2 = set() #(r - c)

res = []

def backtrack(r):
    if r == n:
        temp = ['  '.join(row) for row in board]
        res.append(temp)

        return
    
    for c in range(n):
        if c in col or (r + c) in diag1 or (r - c) in diag2 :
            continue

        col.add(c)
        diag1.add(r + c)
        diag2.add(r - c)
        board[r][c] = 'Q'

        backtrack(r + 1)

        col.remove(c)
        diag1.remove(r + c)
        diag2.remove(r - c)
        board[r][c] = '-'

backtrack(0)
show = True if input(f'There are {len(res)} solutions. Do you wish to see one of the solutions?(y/n) ').lower() == 'y' else False
if show:
    print('One of the solution is:')
    print(*res[0], sep='\n\n', end='\n\n')
