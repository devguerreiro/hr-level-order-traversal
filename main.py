from collections import deque

def levelOrder(root):
    queue = deque([root])
    output = []
    
    while queue:
        node = queue.popleft()
        
        output.append(str(node))
        
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    print(" ".join(output))
