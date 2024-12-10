class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)
        print(f"{item} pushed to stack.")

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def peek(self):
        """Return the top item of the stack without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Display the entire stack."""
        if not self.is_empty():
            print("Stack contents:", self.stack)
        else:
            print("Stack is empty.")

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    stack.display()
    print("Popped element:", stack.pop())
    print("Popped element:", stack.pop())
    print("Popped element:", stack.pop())


# Output: python Stack.py 
# 10 pushed to stack.
# 20 pushed to stack.
# 30 pushed to stack.
# Stack contents: [10, 20, 30]
# Top element: 30
# Popped element: 30
# Stack contents: [10, 20]
# Popped element: 20
# Popped element: 10
# Stack is empty. Cannot pop.
# Popped element: None