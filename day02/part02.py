import os

def is_safe(report: list) -> bool:
    # There are two things to check:
    # - are levels all increasing or all decreasing?
    # - all steps should be of absolute value of 1, 2 or 3.
    if len(report) < 2: return True
    increasing = report[0] < report[1]
    for a, b in zip(report[:-1], report[1:]):
        step = abs(a-b)
        if ((a < b) != increasing) or not (1 <= step and step <= 3):
            return False
    return True

def one_removed(report: list) -> list:
    """
    Given a list, returns a list of list, each one of those list being the original list with an element removed.
    """
    return [report[:i]+report[i+1:] for i in range(len(report))]


def is_safe_relaxed(report: list) -> bool:
    """
    Same as is_safe but allows for one mistake.
    """
    return is_safe(report) or any([is_safe(aux_report) for aux_report in one_removed(report)])

def result(data: list) -> int:
    """
    Returns the number of safe reports given a list of reports (each report being a list of levels).
    """
    return sum([is_safe_relaxed(report) for report in data])
            
if __name__ == "__main__":
    with open("./day02/input.txt") as f:
        content = f.read()
    # uterlly unoptimized but for day 2 this is not an issue. We will care about time complexity on day 15 (:
    data = [[int(e) for e in line.split()] for line in content.split("\n") if line != ""]
    print(result(data))

