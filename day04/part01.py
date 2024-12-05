def result(grid: list) -> int:
    word = "XMAS"
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1), (0, -1),  # Horizontal
        (1, 0), (-1, 0),  # Vertical
        (1, 1), (-1, -1), # Diagonal Left
        (1, -1), (-1, 1)  # Diagonal Right
    ]
    
    def is_in_grid(x, y):
        """
        Check if the coordinates are within grid bounds.
        """
        return 0 <= x < rows and 0 <= y < cols

    def can_fit_in_direction(x, y, dx, dy):
        """
        Check if the word can fit in the grid starting from (x, y) in direction (dx, dy).
        """
        nx, ny = x + (word_len - 1) * dx, y + (word_len - 1) * dy
        return is_in_grid(nx, ny)

    def check_direction(x, y, dx, dy):
        """
        Check if the word exists starting at (x, y) in direction (dx, dy).
        """
        for k in range(word_len):
            nx, ny = x + k * dx, y + k * dy
            if grid[nx][ny] != word[k]:
                return False
        return True

    count = 0
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if can_fit_in_direction(i, j, dx, dy) and check_direction(i, j, dx, dy):
                    count += 1
    return count

if __name__ == "__main__":
    with open("./day04/input.txt") as f:
        content = f.read().strip()
    grid = content.split("\n")
    print(result(grid))
