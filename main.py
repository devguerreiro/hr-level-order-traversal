def levelOrder(root):
    queue = [root]
    output = []
    
    while queue:
        first = queue.pop(0)
        
        output.append(str(first))
        
        if first.left is not None:
            queue.append(first.left)
        if first.right is not None:
            queue.append(first.right)

    print(" ".join(output))
