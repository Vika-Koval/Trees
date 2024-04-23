class Solution:
    def deleteNode(self, root, key):
        now, node = self.find(root, key)
        if node is None:
            return root
        if node.right is None or node.left is None:
            substitute= None
            if node.left is not None:
                substitute = node.left
            else:
                substitute = node.right
            if now is None:
                return substitute
            elif now.left is node:
                now.left = substitute
            else:
                now.right = substitute
            return root
        parent = None
        min_n = node.right
        while min_n.left:
            parent = min_n
            min_n = min_n.left
        if parent is not None:
            parent.left = min_n.right
        else:
            node.right = min_n.right
        node.val = min_n.val
        return root

    def find(self, root, key):
        now = None
        while root and root.val != key:
            now = root
            if key < root.val:
                root = root.left
            else:
                root = root.right
        return (now, root)
