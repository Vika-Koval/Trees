def tree_by_levels(node):
    print(node)
    if node:
        res = []
        a = [node]
        while len(a) > 0:
            nodes = a.pop(0)
            if nodes is None:
                continue
            res.append(nodes.value)
            a.append(nodes.left)
            a.append(nodes.right)
        return res
    return []
