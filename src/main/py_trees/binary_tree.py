class BinaryTreeNode:
    def __init__(self, value, left_node, right_node):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

    @property
    def get_value(self):
        return self.value

    @property
    def get_left_node(self):
        return self.left_node

    @property
    def get_right_node(self):
        return self.right_node
