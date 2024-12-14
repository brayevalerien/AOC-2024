from copy import deepcopy

guard_directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def print_grid(grid):
    print("  " + " ".join([str(e) for e in range(len(grid[0]))]))
    for i, line in enumerate(grid):
        print(i, " ".join(line))

def get_guard_position(grid: list[list[str]]) -> tuple[int]:
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char in guard_directions:
                return i, j
    return None

def rotate_guard(current_guard: str) -> str:
    """
    Given the string representation of a guard, returns the representation of the guard after a 90° rotation (clockwise).
        e.g. given "v", returns "<"
    """
    # it feels like there is a more elegant/pythonic solution to it, but this works
    char_list = list(guard_directions.keys())
    if current_guard == char_list[-1]:
        return char_list[0]
    return char_list[char_list.index(current_guard)+1]

def get_visited_positions(grid: list[list[str]]) -> set[tuple[int]] | None:
    """
    Given a grid in the form of the puzzle input, returns a set with all visited positions as tuples (x, y).
    If a loop is formed, as soon as it's detected, return None.
    """
    grid = deepcopy(grid)
    step = 0 # number of actual step the guard took (one move forward)
    rows, columns = len(grid), len(grid[0])
    visited = set()

    def is_in_grid(x: int, y: int) -> bool:
        return 0<=x<rows and 0<=y<columns

    x, y = get_guard_position(grid)
    while True:
        visited.add((x, y))
        dx, dy = guard_directions[grid[x][y]]
        nx, ny = x+dx, y+dy

        if not is_in_grid(nx, ny):
            # guard left the grid, mapping is complete
            return visited
        elif grid[nx][ny] == grid[x][y] or rows*columns<step:
            # if crossing a visited position and in the same orientation, the guard is stuck in a loop
            # it's also same to assume that if the guard stepped more than there are cells in the grid, its stuck in a loop (ewwww heuristic... this could be improved but my code is buggy otherwise.)
            return None
        elif grid[nx][ny] == "#":
            # rotate the guard without changing its position
            grid[x][y] = rotate_guard(grid[x][y])
        else:
            grid[nx][ny] = grid[x][y] # move the guard forward            
            x, y = nx, ny # update guard position
            step += 1

def result(grid: list[list[str]]) -> int:
    result = 0
    for position in get_visited_positions(grid):
        # for each position that would be visited by the guard in the initial grid (excluding the starting position), try to place an obstable and see if it loops. If it does, increment the result.
        # Note: this semi-brute force aproach take 1~2 minutes to run, it could use some caching technique to avoid reconputing the guard path before the obstacle.
        if not position == get_guard_position(grid):
            x, y = position
            ngrid = deepcopy(grid)
            ngrid[x][y] = "#"
            if not get_visited_positions(ngrid):
                result += 1
    return result

if __name__ == "__main__":
    with open("./day06/input.txt") as f:
        content = f.read()
    print(result([[char for char in line] for line in content.splitlines()]))
