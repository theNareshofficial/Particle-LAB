import java.util.*;

// Main class
public class StackGeneric {
    public static void main(String[] args) {
        int[] ia = {1, 2, 3, 4, 5};
        char[] ca = {'A', 'B', 'C', 'D', 'E'};

        // Create integer and character stack instances
        Stack<Integer> ist = new Stack<>(5);
        Stack<Character> cst = new Stack<>(5);

        // Push elements into the integer stack
        System.out.println("\nPushing the elements in the integer stack:");
        for (int i = 0; i < 5; i++) {
            ist.push(ia[i]);
            System.out.println("Pushed: " + ia[i]);
        }

        // Push elements into the character stack
        System.out.println("\nPushing the elements in the character stack:");
        for (int i = 0; i < 5; i++) {
            cst.push(ca[i]);
            System.out.println("Pushed: " + ca[i]);
        }

        // Pop elements from the character stack
        System.out.println("\nPopping the elements from the character stack:");
        for (int i = 0; i < 2; i++) {
            System.out.println("Popped: " + cst.pop());
        }

        // Pop elements from the integer stack
        System.out.println("\nPopping the elements from the integer stack:");
        for (int i = 0; i < 5; i++) {
            System.out.println("Popped: " + ist.pop());
        }

        // Attempt to pop again from the integer stack
        System.out.println("\nPerforming one more pop on the integer stack:");
        System.out.println("Popped: " + ist.pop());
    }
}

// // Output
// Pushing the elements in the integer stack:
// Pushed: 1
// Pushed: 2
// Pushed: 3
// Pushed: 4
// Pushed: 5

// Pushing the elements in the character stack:
// Pushed: A
// Pushed: B
// Pushed: C
// Pushed: D
// Pushed: E

// Popping the elements from the character stack:
// Popped: E
// Popped: D

// Popping the elements from the integer stack:
// Popped: 5
// Popped: 4
// Popped: 3
// Popped: 2
// Popped: 1

// Performing one more pop on the integer stack:
// Stack is empty
// Popped: null
