
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build_next_tree_from_list(v) -> Node:
    levels = []
    current_level = []
    i = 0
    is_left = True
    for value in v:
        if value == '#':
            levels.append(current_level)
            i = 0
            current_level = []
            is_left = True
        else:
            node = Node(value)
            if current_level:
                current_level[-1].next = node
            current_level.append(node)
            if levels:
                if is_left:
                    levels[-1][i].left = node
                    is_left = False
                else:
                    levels[-1][i].right = node
                    is_left = False
                    i += 1
    return levels[0][0] if levels else None
