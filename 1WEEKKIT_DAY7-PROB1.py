def preOrderRecursive(root):
    """
    Pre-order traversal (recursive version):
    - Visit the root node
    - Traverse the left subtree
    - Traverse the right subtree
    """
    if root is None:
        return

    # Process the current node first
    print(root.info, end=" ")

    # Recursively traverse the left child
    preOrderRecursive(root.left)

    # Recursively traverse the right child
    preOrderRecursive(root.right)


# -------------------------------
# ITERATIVE PRE-ORDER TRAVERSAL
# -------------------------------
def preOrderIterative(root):
    """
    Pre-order traversal (iterative version using a stack):
    - Use a stack to simulate the call stack
    - Push the right child first, then the left, so that left is processed first
    """
    if root is None:
        return

    stack = [root]

    while stack:
        # Pop the top node and process it
        node = stack.pop()
        print(node.info, end=" ")

        # Push right child first so it's processed after the left child
        if node.right:
            stack.append(node.right)

        # Push left child
        if node.left:
            stack.append(node.left)

