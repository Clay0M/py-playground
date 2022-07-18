class BinaryTreeNode:

    def __init__(self, node_value, left_node, right_node):
        self.node_value = node_value
        assert isinstance(left_node, BinaryTreeNode or type(None))
        self.left_node = left_node
        assert isinstance(right_node, BinaryTreeNode or type(None))
        self.right_node = right_node


class BinaryTree:

    def __init__(self, root_node):
        assert isinstance(root_node, BinaryTreeNode)
        self.root_node = root_node
