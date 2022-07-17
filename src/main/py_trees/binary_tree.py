class BinaryTreeNode:
    def __init__(self, node_value, left_node, right_node):
        self.node_value = node_value
        assert isinstance(left_node, BinaryTreeNode or type(None))
        self.left_node = left_node
        assert isinstance(right_node, BinaryTreeNode or type(None))
        self.right_node = right_node

    @property
    def get_node_value(self):
        return self.node_value

    @property
    def get_left_node(self):
        return self.left_node

    @property
    def get_right_node(self):
        return self.right_node
