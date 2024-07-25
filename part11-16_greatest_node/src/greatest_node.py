# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root:Node):
    if root is None:
        return None
    
    great = root.value
    left = greatest_node(root.left_child)
    right = greatest_node(root.right_child)

    if left is not None:
        great = max(great, left)
    if right is not None:
        great = max(great, right)
    
    return great


    

