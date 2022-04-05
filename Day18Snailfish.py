snail_numbers = []

with open("day18SnailTest.txt") as f:
    raw_data = f.read().strip().split("\n")
data = [eval(line) for line in raw_data]


class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        if isinstance(self.val, int):
            return str(self.val)
        return f"[{str(self.left)},{str(self.right)}]"


def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)


def reduce(root):
    done = True

    stack = [(root, 0)]

    while len(stack) > 0:
        node, depth = stack.pop()

        done = True

        if node == None:
            continue

        condition = (node.left is None and node.right is None) or \
                    (node.left.val is not None and node.right.val is not None)

        if depth >= 4 and node.val is None and condition:
            prev_node = node.left
            cur_node = node
            while cur_node is not None and (cur_node.left == prev_node or cur_node.left is None):
                prev_node = cur_node
                cur_node = cur_node.parent

            if cur_node is not None:
                cur_node = cur_node.left
                while cur_node.val is None:
                    if cur_node.right is not None:
                        cur_node = cur_node.right
                    else:
                        cur_node = cur_node.left

                cur_node.val += node.left.val

            prev_node = node.right
            cur_node = node
            while cur_node is not None and (cur_node.right == prev_node or cur_node.right is None):
                prev_node = cur_node
                cur_node = cur_node.parent

            if cur_node is not None:
                cur_node = cur_node.right
                while cur_node.val is None:
                    if cur_node.left is not None:
                        cur_node = cur_node.left
                    else:
                        cur_node = cur_node.right

                cur_node.val += node.right.val

            node.val = 0
            node.left = None
            node.right = None

            done = False
            break

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))

    if not done:
        reduce(root)
        return

    stack = [root]

    while len(stack) > 0:
        node = stack.pop()

        if node is None:
            continue

        if node.val is not None:
            assert node.left is None and node.right is None

            if node.val >= 10:
                node.left = Node(node.val // 2)
                node.right = Node(node.val - (node.val // 2))
                node.left.parent = node
                node.right.parent = node
                node.val = None

                done = False
                break

        stack.append(node.right)
        stack.append(node.left)

    if not done:
        reduce(root)


def createtree(keys):
    root = Node()

    if isinstance(keys, int):
        root.val = keys
        return root

    root.left = createtree(keys[0])
    root.right = createtree(keys[1])
    root.right.parent = root
    root.left.parent = root

    reduce(root)

    return root


def add(A, B):
    root = Node()
    root.left = A
    root.right = B
    root.left.parent = root
    root.right.parent = root

    reduce(root)

    return root


def magnitude(root):
    if isinstance(root.val, int):
        return root.val

    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


i, n = 1, len(data)
root = createtree(data[0])
magnitude_list = []
# while i < n:
#     added = createtree(data[i])
#     root = add(root, added)
#     i += 1

for i in range(n):
    for j in range(i + 1, n):
        A, B = createtree(data[i]), createtree(data[j])
        root_AB = add(A, B)
        root_BA = add(B, A)
        magnitude_list.append(magnitude(root_AB))
        magnitude_list.append(magnitude(root_BA))

print(max(magnitude_list))
print(magnitude(root))
