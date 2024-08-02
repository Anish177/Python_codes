#Not Solvable:
#A = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
#S = [[1, 2, 3], [5, 6, 8], [0, 7, 4]]


#Solvable:
#A = [[0,2,3], [1,4,5], [8,7,6]]
#S = [[1,2,3], [8,0,4], [7,6,5]]

# another possible solution: two visited lists - one with all visited states and other for current?


"""
Solves 3 x 3 puzzle (8-Puzzle).
Could be generalized to n x n puzzles as well.

Uses Greedy Best First Search to find solution.

Note: Some puzzles are unsolvable due to parity issues.
This approach does not precheck for solvability and considers a puzzle unsolvable when the iteration limit is reached.


Approximate Time Complexity: O(4 ^ d)

Did you know? Most solvable 8-puzzles can be solved with at most 31 moves.

Possible future improvements:
1. Reduce redundancy in the code.
2. Use sets instead of lists for visited states to improve lookup efficiency.
"""

from ast import literal_eval
from contextlib import suppress
from copy import deepcopy

inp = input

A = [
    [int(inp('Enter value for (1, 1): ')), int(inp('Enter value for (1, 2): ')), int(inp('Enter value for (1, 3): '))],
    [int(inp('Enter value for (2, 1): ')), int(inp('Enter value for (2, 2): ')), int(inp('Enter value for (2, 3): '))],
    [int(inp('Enter value for (3, 1): ')), int(inp('Enter value for (3, 2): ')), int(inp('Enter value for (3, 3): '))]
    ]

print('Given puzzle is:')
print(*A, sep = '\n')
print()


S = [
    [int(inp('Enter value for (1, 1): ')), int(inp('Enter value for (1, 2): ')), int(inp('Enter value for (1, 3): '))],
    [int(inp('Enter value for (2, 1): ')), int(inp('Enter value for (2, 2): ')), int(inp('Enter value for (2, 3): '))],
    [int(inp('Enter value for (3, 1): ')), int(inp('Enter value for (3, 2): ')), int(inp('Enter value for (3, 3): '))]
    ]

print('To solve it into:')
print(*S, sep = '\n')
print()


#finding cost as tiles out of place
def cost(A, S):
    h = 9

    for k in range(3):
        for l in range(3):
            if A[k][l] == S[k][l]:
                h -= 1              
    return h

#finding possible paths
def possible_paths(temp0, visited_final):
    paths={}

    #finding 0
    with suppress(StopIteration):
        for i in range(3):
            for j in range(3):
                if temp0[i][j] == 0:
                    raise StopIteration
    
    #-----

    #switching 0 and adding to possible paths

    if i != (len(temp0) - 1):
        temp = deepcopy(temp0)
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0

        if temp not in visited_final:
            paths[str(temp)] = cost(temp, S)

    if j != (len(temp0) - 1):
        temp = deepcopy(temp0)
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0

        if temp not in visited_final:
            paths[str(temp)] = cost(temp, S)

    if i != 0:
        temp = deepcopy(temp0)
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0

        if temp not in visited_final:
            paths[str(temp)] = cost(temp, S)

    if j != 0:
        temp = deepcopy(temp0)
        temp[i][j] =  temp[i][j - 1]
        temp[i][j - 1] = 0

        if temp not in visited_final:
            paths[str(temp)] = cost(temp, S)
    #-----

    return paths

#-----

#solving the puzzle
def solve(temp0: list, S: list) -> None:
    visited_current = []
    visited_final = deepcopy(visited_current)
    visited_current.append(temp0)
    count = 0

    while temp0 != S:

        paths = possible_paths(temp0, visited_final)
        #print(paths)

        #changing temp0 and finding solution
        try:
            temp0 = literal_eval(min(paths, key = paths.get))
            if temp0 == S:
                print('Solved.')
                break
            if temp0 not in visited_final:
                visited_current.append(temp0)
                visited_final.append(temp0)

        except IndexError:
            temp0 = visited_current.pop()

        finally:
            print('Current state:')
            print(*temp0, sep='\n')
            print()

        #-----

        #in case the puzzle is not solvable
        count += 1

        #print(count)
        if count > 1000:
            print('Could not find solve in 31 iterations.')
            break

        #-----
#-----


solve(A, S)

# easter egg: this was one of two of the first programs I have ever written
