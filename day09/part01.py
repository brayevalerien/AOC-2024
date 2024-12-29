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
    Given the expanded disk state, sorts the blocks to move file blocks from the end of the disk to the empty blocks at the beginning of the disk.
    """
    # idea:
    # 1. go in reverse order in the list and for each block with a file, move it's content to the first empty block.
    # 2. remove all empty blocks at the end of the list

    # step 1.
    for i in range(len(disk)):
        block_index = len(disk) - i - 1
        block = disk[block_index]
        next_empty = disk.index(".")
        if block_index <= next_empty:
            # then whole disk is sorted, go to step 2.
            break
        if block != ".":
            disk[next_empty] = block
            disk[block_index] = "."
    # step 2.
    disk = disk[: disk.index(".")]
    return disk


def checksum(disk: list[str]) -> int:
    """
    Computes the checksum of a sorted disk (sum of each block position multiplied by the file index of its content).
    """
    return sum([i * int(block) for i, block in enumerate(disk)])


def result(content: str) -> int:
    return checksum(sort_expanded(expand(content)))


if __name__ == "__main__":
    with open("day09/input.txt") as f:
        content = f.read()
    print(result(content))
