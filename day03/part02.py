import re

def get_multiplications(input: str) -> list:
    """
    Gets the raw input with corrupted instructions and extracts all multiplications.
    Return a list of tuples of 2 int, each tuple corresponding to a valid mul(x,y) instruction where x and y are 1-3 digits integers.
    """
    # the following regex matches only valid "mul" instructions and their arguments
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    mul_strings = re.findall(pattern, input)
    result = []
    for mul in mul_strings:
        arguments = re.findall(r"\d{1,3}", mul)
        result.append((int(arguments[0]), int(arguments[1])))
    return result

def get_conditions(input: str) -> list:
    """
    Gets the raw input and extracts all conditions (do() and don't()) along with their positions.
    Return a list of tuples where each tuple contains the condition ('do' or 'don't') and its index in the input.
    """
    pattern = r"(do\(\)|don't\(\))"
    matches = [(m.group(), m.start()) for m in re.finditer(pattern, input)]
    return [(m[0][:-2], m[1]) for m in matches]

def filter_multiplications(input: str, multiplications: list) -> list:
    """
    Given the input string and a list of multiplications, filters the multiplications based on the most recent 'do' or 'don't' condition.
    """
    conditions = get_conditions(input)
    if not conditions:
        return multiplications # iff no conditions are present, all multiplications are enabled
    result = []
    last_condition = "do"
    condition_index = 0
    condition_positions = [c[1] for c in conditions]
    for i, (x, y) in enumerate(multiplications):
        mul_position = re.search(rf"mul\({x},{y}\)", input).start()
        while condition_index < len(condition_positions) and condition_positions[condition_index] < mul_position:
            last_condition = conditions[condition_index][0]
            condition_index += 1
        if last_condition == "do":
            result.append((x, y))
    return result

def process(multiplications: list) -> int:
    """
    Given a list of multiplications following the format returned by get_multiplications, computes the sum of all results of the multiplications.
    """
    return sum([e[0]*e[1] for e in multiplications])

def result(input: str) -> int:
    multiplications = get_multiplications(input)
    filtered_multiplications = filter_multiplications(input, multiplications)
    return process(filtered_multiplications)

if __name__ == "__main__":
    with open("day03/input.txt") as f:
        content = f.read()
    print(result(content))
