import re

def get_multiplications(input: str) -> list:
    """
    Gets the raw input with corrupted instructions and extract all multiplications. Return a list of tuples of 2 int, each tuple corresponding to a valid mul(x,y) instruction where x and y are 1-3 digits integers.
    """
    # the following regex matches only valid "mul" instructions and their arguments
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    mul_strings = re.findall(pattern, input)
    result = []
    for mul in mul_strings:
        arguments = re.findall(r"\d{1,3}", mul)
        result.append((int(arguments[0]), int(arguments[1])))
    return result

def process(multiplications: list) -> int:
    """
    Given a list of multiplications following the format returned by get_multiplications, computes the sum of all results of the multiplications
    """
    return sum([e[0]*e[1] for e in multiplications])

def result(input: str) -> int:
    multiplications = get_multiplications(input)
    return process(multiplications)

if __name__ == "__main__":
    with open("day03/input.txt") as f:
        content = f.read()
    print(result(content))
