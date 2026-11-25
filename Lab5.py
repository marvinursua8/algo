from collections import deque
class TreeNode:
    def __init__(self, val, children=None):
        self.val = val
        self.children = [] if children is None else children

    def valuesDFS(self):
        result = []
        stack = [self]

        while stack:
            node = stack.pop()
            result.append(node.val)

            for child in reversed(node.children):
                stack.append(child)

        return result


    def valuesBFS(self):
        result = []
        queue = deque([self])

        while queue:
            node = queue.popleft()
            result.append(node.val)

            for child in node.children:
                queue.append(child)

        return result


    def countLeaves(self):
        result = []
        count = 0
        stack = [self]

        while stack:
            node = stack.pop()

            if not node.children:
                result.append(node.val)
                count += 1
            else:
                for child in reversed(node.children):
                    stack.append(child)

        return result, count

    def find(self, val):
        stack = [self]

        while stack:
            node = stack.pop()

            if node.val == val:
                return node

            for child in reversed(node.children):
                stack.append(child)


    def findShallowest(self,val):
        queue = [self]

        while queue:
            node = queue.pop(0)


            if node.val == val:
                return node

            for child in (node.children):
                queue.append(child)

        return None




h = TreeNode("H")
i = TreeNode("I")
j = TreeNode("J")
k = TreeNode("K")

e = TreeNode("E")
f = TreeNode("F", [h, i])
g = TreeNode("G", [j, k])

b = TreeNode("B", [e, f])
c = TreeNode("C")
d = TreeNode("D", [g])

tree = TreeNode("A", [b, c, d])


test = print(tree.findShallowest("F"))

print(test.children)