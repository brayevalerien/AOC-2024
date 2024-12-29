def expand(content: str) -> list[str]:
    """
    Given the raw disk map, expands it to show the full disk representation.
    e.g. given 12345, returns 0..111....22222
    Note: since the actual inputs have files with indices greater than 9, we treat the disk as a list, each element being a block (instead of a simple string that works for the examples).
    """
    file_index = 0
    index = 0
    result = []
    while index < len(content):
        result += [str(file_index)] * int(content[index])
        if index + 1 < len(content):
            result += ["."] * int(content[index + 1])
        file_index += 1
        index += 2
    return result


def sort_expanded(disk: list[str]) -> list[str]:
    """
    Given the expanded disk state, sorts the blocks to move files from the end of the disk to the beginning, keeping them contiguous.
    Note: this is highly unoptimized.
    """
    # idea: go in reverse order in the list and for each file, find an empty area with enough space to move it to the left. Don't move it if no such space is found.

    def find_empty(size: int) -> int:
        """
        Returns the index of the first block of a contiguous sequence of empty blocks on the disk. Returns the leftmost solution if there are multiple ones and -1 if there is no solution.
        """
        for i in range(len(disk) - size):
            if all([block == "." for block in disk[i : i + size]]):
                return i
        return -1

    # iterate through the files in decreasing file order
    file_indices = [int(block) for block in disk if block != "."]
    for file in range(max(file_indices), -1, -1):
        file = str(file)
        # 1. find the first element and the size of the current file
        block_index = disk.index(file)
        size = disk.count(file)  # this assumes all files are contiguous
        # 2. if there is a fitting empty space AND it is to the file's left, move file to this space
        empty_index = find_empty(size)
        if 0 <= empty_index and empty_index < block_index:
            for i in range(size):
                disk[empty_index + i] = file
                disk[block_index + i] = "."
    return disk


def checksum(disk: list[str]) -> int:
    """
    Computes the checksum of a sorted disk (sum of each block position multiplied by the file index of its content).
    """
    return sum([i * int(block) for i, block in enumerate(disk) if block != "."])


def result(content: str) -> int:
    return checksum(sort_expanded(expand(content)))


if __name__ == "__main__":
    with open("day09/input.txt") as f:
        content = f.read()
    print(result(content))
