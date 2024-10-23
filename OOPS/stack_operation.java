/*
To develop a java program for stack data structure using class and object
*/

class Stack {
    private int arr[];
    private int top;
    private int capacity;

    // Constructor to initialize the stack
    Stack(int size) {
        arr = new int[size];
        capacity = size;
        top = -1;
    }

    // Method to add an element `x` to the stack
    public void push(int x) {
        if (isFull()) {
            System.out.println("Overflow\nProgram Terminated");
            System.exit(-1);
        }
        System.out.println("Inserting " + x);
        arr[++top] = x;
    }

    // Method to remove the top element from the stack
    public int pop() {
        if (isEmpty()) {
            System.out.println("Underflow\nProgram Terminated");
            System.exit(-1);
        }
        System.out.println("Removing " + peek());
        return arr[top--];
    }

    // Method to return the top element of the stack
    public int peek() {
        if (!isEmpty()) {
            return arr[top];
        } else {
            System.exit(-1);
        }
        return -1; // Unreachable, but necessary for compilation
    }

    // Method to return the size of the stack
    public int size() {
        return top + 1;
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return top == -1; // or return size() == 0;
    }

    // Method to check if the stack is full
    public boolean isFull() {
        return top == capacity - 1; // or return size() == capacity;
    }
}

class Main {
    public static void main(String[] args) {
        Stack stack = new Stack(3);

        // Demonstrate push operation
        stack.push(1); // inserting 1 in the stack
        stack.push(2); // inserting 2 in the stack

        // Demonstrate pop operation
        stack.pop();   // removing the top element (2)
        stack.pop();   // removing the top element (1)

        // Insert new element into the stack
        stack.push(3);
        
        // Peek top element
        System.out.println("The top element is " + stack.peek());

        // Display the size of the stack
        System.out.println("The stack size is " + stack.size());

        // Remove the top element
        stack.pop();   // removing the top element (3)

        // Check if the stack is empty
        if (stack.isEmpty()) {
            System.out.println("The stack is empty");
        } else {
            System.out.println("The stack is not empty");
        }
    }
}

/*
Output:
*/