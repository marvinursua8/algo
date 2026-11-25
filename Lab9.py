class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children
















def make_tree():
    return TreeNode(8, [
        TreeNode(3, [
            TreeNode(1),
            TreeNode(6, [
                TreeNode(4),
                TreeNode(7)
            ])
        ]),
        TreeNode(10, [
            TreeNode(14, [
                TreeNode(13)
            ])
        ])
    ])