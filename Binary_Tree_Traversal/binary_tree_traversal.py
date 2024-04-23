# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    a = []
    if node.data:
        a.append(node.data)
    if node.left:
        a.extend(pre_order(node.left))
    if node.right:
        a.extend(pre_order(node.right))
    return a

# In-order traversal
def in_order(node):
    if node is None:
        return []
    a = []
    if node.left:
        a.extend(in_order(node.left))
    if node.data:
        a.append(node.data)
    if node.right:
        a.extend(in_order(node.right))
    return a

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    a = []
    if node.left:
        a.extend(post_order(node.left))
    if node.right:
        a.extend(post_order(node.right))
    if node.data:
        a.append(node.data)
    return a
