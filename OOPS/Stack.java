import java.util.*;

// Define a generic class
public class Stack<T> {
    public ArrayList<T> obj;

    // Constructor
    public Stack(int size) {
        obj = new ArrayList<>(size);
    }

    // Push method to add elements
    public void push(T item) {
        obj.add(item);
    }

    // Pop method to remove and return elements
    public T pop() {
        if (obj.isEmpty()) {
            System.out.println("\nStack is empty");
            return null;
        }
        return obj.remove(obj.size() - 1);
    }
}
