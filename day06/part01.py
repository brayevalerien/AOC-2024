guard_directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

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

def mapped(grid: list[list[str]]) -> list[str]:
    """
    Given a grid in the form of the puzzle input, returns the same grid but where position where the guard walked marked with "X"s.
    """
    rows, columns = len(grid), len(grid[0])

    def is_in_grid(x: int, y: int) -> bool:
        return 0<=x<rows and 0<=y<columns

    while True:
        x, y = get_guard_position(grid)
        dx, dy = guard_directions[grid[x][y]]
        nx, ny = x+dx, y+dy
        
        if not is_in_grid(nx, ny):
            # guard left the grid, mapping is complete
            grid[x][y] = "X" # simply mark past location as visited
            return grid
        if grid[nx][ny] == "#":
            # rotate the guard without changing its position
            grid[x][y] = rotate_guard(grid[x][y])
        else:
            grid[nx][ny] = grid[x][y] # move the guard forward            
            grid[x][y] = "X" # mark past location as visited

def result(grid: list[str]) -> int:
    return sum([line.count("X") for line in mapped(grid)])

if __name__ == "__main__":
    with open("./day06/input.txt") as f:
        content = f.read()
    print(result([[char for char in line] for line in content.splitlines()]))