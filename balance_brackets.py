def isBalanced(s): 
    # Initialize an empty stack to track opening brackets
    stack = []
    
    # Dictionary to match closing brackets with their corresponding opening brackets
    matching = {')': '(', '}': '{', ']': '['}
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an opening bracket, push it to the stack
        if char in '({[':
            stack.append(char)
        else:
            # If the character is a closing bracket, check if it matches the top of the stack
            if not stack or stack[-1] != matching[char]:
                return "NO"  # If not, return "NO"
            stack.pop()  # If they match, pop the top element from the stack
    
    # After the loop, if the stack is empty, it means all brackets matched, return "YES"
    return "YES" if not stack else "NO"  # If stack is not empty, return "NO"
