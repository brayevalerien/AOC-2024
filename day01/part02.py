import os

def parse(content: str) -> tuple:
    """
    Parses the content of the input file.
    Given the raw content of the input file, returns the left and right lists.
    """
    lines = content.split("\n")
    # Check line length to avoid errors on empty lines
    split_lines = [line.split() for line in lines if len(line)!=0]
    # Pretty sure there is a better way to do that but no time to think about it
    left = [e[0] for e in split_lines]
    right = [e[1] for e in split_lines]
    return left, right

def compute_result(left: list, right: list) -> int:
    """
    Given the left and right lists, returns the similarity score.
    Similarity score is computed by multiplying each number in the left list by the number of time it appears in the right list and then summing the results.
    """
    return sum([int(l)*right.count(l) for l in left])

if __name__ == "__main__":
    with open("day01/input.txt") as f:
        content = f.read()
    left, right = parse(content)
    result = compute_result(left, right)
    print(result)
