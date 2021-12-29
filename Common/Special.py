
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_special_tree_from_string(s: str) -> Node:

    def build_levels(s: str):
        levels = []
        current_level = 0
        prev = None
        for c in s[1:-1].split(","):
            if not c:
                break
            if current_level == len(levels):
                levels.append([])
            if c == '#':
                current_level += 1
                prev = None
            else:
                node = Node(int(c))
                if prev:
                    prev.next = node
                levels[current_level].append(node)
                prev = node
        return levels

    levels = build_levels(s)
    if not levels:
        return None

    m = len(levels)
    for level in range(m-1):
        j = 0
        for node in levels[level]:
            if j == len(levels[level+1]):
                break
            node.left = levels[level+1][j]
            j += 1
            if j == len(levels[level+1]):
                break
            node.right = levels[level + 1][j]
            j += 1

    return levels[0][0]

