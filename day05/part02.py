from collections import defaultdict, deque

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
            if update.index(b) < update.index(a):
                return False
    return True

def reorder_update(update: list[int], rules: list[tuple[int]]) -> list[int]:
    """
    Sorts an update using the rules orders.
    Uses the Kahn's algorithm for topological sort:
    https://leetcodethehardway.com/tutorials/graph-theory/kahns-algorithm
    """
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    for a, b in rules:
        if a in update_set and b in update_set:
            graph[a].append(b)
            in_degree[b] += 1
            if a not in in_degree:
                in_degree[a] = 0
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    while queue:
        node = queue.popleft()
        sorted_update.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_update

def result(rules: list[tuple[int]], updates: list[list[int]]) -> int:
    reordered_updates = [reorder_update(update, rules) for update in updates if not is_valid(update, rules)]
    return sum(update[len(update)//2] for update in reordered_updates)

if __name__ == "__main__":
    with open("./day05/input.txt") as f:
        raw_rules, raw_updates = f.read().split("\n\n")
    rules = parse_rules(raw_rules)
    updates = parse_updates(raw_updates)
    print(result(rules, updates))
