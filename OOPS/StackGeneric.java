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
