def parse_rules(raw_rules: str) -> list[tuple[int]]:
    return [tuple(map(int, x.split("|"))) for x in raw_rules.splitlines()]

def parse_updates(raw_updates: str) -> list[list[int]]:
    return [list(map(int, x.split(","))) for x in raw_updates.splitlines()]

def is_valid(update: list[int], rules: list[tuple[int]]) -> bool:
    """
    Checks if an update follows all ordering rules in a list of rules.
    """
    for a, b in rules:
        if a in update and b in update:
            # check if a appears before b in the update    
            if update.index(b) < update.index(a):
                return False
    return True

def result(rules: list[tuple[int]], updates: list[list[int]]) -> int:
    valid_updates = [update for update in updates if is_valid(update, rules)]
    return sum(update[len(update)//2] for update in valid_updates)

if __name__ == "__main__":
    with open("./day05/input.txt") as f:
        raw_rules, raw_updates = f.read().split("\n\n")
    rules = parse_rules(raw_rules)
    updates = parse_updates(raw_updates)
    print(result(rules, updates))
