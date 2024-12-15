def parse(content: str) -> list[tuple[int]]:
    """
    Given the raw content of the input file, return a list of equation, each one in the form of a tuple, firt element being the result and the other elements bein the terms of the equation.
    """
    result = []
    for line in content.splitlines():
        split = line.split(": ")
        result.append((int(split[0]), *[int(e) for e in split[1].split()]))
    return result


def is_obtainable(eq_result: int, eq_terms: list[int]) -> bool:
    """
    Given an equation, returns True iff the result can be obtained by adding and multiplying the others.
    """
    if len(eq_terms) == 1:
        # base case: only one term left, must be equal to the result
        return eq_result == eq_terms[0]
    if eq_result % eq_terms[-1] == 0:
        obtainable_with_times = is_obtainable(eq_result // eq_terms[-1], eq_terms[:-1])
        obtainable_with_plus = is_obtainable(eq_result - eq_terms[-1], eq_terms[:-1])
        return obtainable_with_times or obtainable_with_plus
    else:
        # if the result is not divisible by the last term, the result minus this last term must be obtainable with the rest of the terms
        return is_obtainable(eq_result - eq_terms[-1], eq_terms[:-1])


def result(equations: list[tuple[int]]) -> int:
    result = 0
    for equation in equations:
        if is_obtainable(equation[0], list(equation)[1:]):
            result += equation[0]
    return result


if __name__ == "__main__":
    with open("./day07/input.txt") as f:
        content = f.read()
    print(result(parse(content)))
