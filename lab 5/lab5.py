class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"TreeNode(contents={repr(self.contents)}, parent-contents={repr(self.parent.contents if self.parent else 'NOPARENT')}, num-children={len(self.children)})"

    def appendChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.append(new_node)
        return new_node

    def prependChild(self, contents):
        new_node = TreeNode(contents)
        new_node.parent = self
        self.children.insert(0, new_node)
        return new_node

    def findRoot(self):
        current = self
        while current.parent is not None:
            current = current.parent
        return current

    def findLeftmostLeaf(self):
        current = self
        while len(current.children) > 0:
            current = current.children[0]
        return current

    def findRightmostLeaf(self):
        current = self
        while len(current.children) > 0:
            current = current.children[-1]
        return current

    def dfs(self, callback):
        callback(self.contents, self)
        for child in self.children:
            child.dfs(callback)


def case1():
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.appendChild("B")
    root.appendChild("C")
    root.appendChild("D")

    print("\ncase1")
    print("I hope the root has 3 children")
    print(root)
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case2():
    #
    #            A
    #         /  |  \
    #        B   C   D
    #
    root = TreeNode("A")
    root.prependChild("C")
    root.appendChild("D")
    root.prependChild("B")

    print("\ncase2")
    print("I hope the root has 3 children")
    print(root)
    print("I hope the leftmost leaf is B, and B's parent is A")
    print(root.findLeftmostLeaf())
    print("I hope the rightmost leaf is D, and D's parent is A")
    print(root.findRightmostLeaf())


def case3():
    #
    #            A
    #         /  |  \
    #        B   C   D
    #        |      / \
    #        E     F   G
    #
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    g = d.prependChild("G")
    f = d.prependChild("F")
    e = b.appendChild("E")

    print("\ncase3")
    for node in [root, b, c, d, e, f, g]:
        r = node.findRoot()
        print("node:", node, "   found root:   ", r, "   is correct tho? ", r == root)

    print("findLeftmostLeaf of root, should be E:", root.findLeftmostLeaf())
    print("findLeftmostLeaf of D, should be F:", d.findLeftmostLeaf())
    print("findRightmostLeaf of D, should be G:", d.findRightmostLeaf())


def case4():
    #
    #            A
    #         /  |  \
    #        B   C   D
    #        |      / \
    #        E     F   G
    #
    root = TreeNode("A")
    c = root.appendChild("C")
    d = root.appendChild("D")
    b = root.prependChild("B")
    d.prependChild("G")
    d.prependChild("F")
    b.appendChild("E")

    print("\ncase4 - DFS from root, expect A B E C D F G:")
    visited = []
    root.dfs(lambda contents, node: visited.append(contents))
    print(visited)

    print("DFS from D, expect D F G:")
    visited = []
    d.dfs(lambda contents, node: visited.append(contents))
    print(visited)


def main(args):
    case1()
    case2()
    case3()
    case4()


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])