class Node:
    """Class to represent a node in a Circular Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Circular Linked List implementation"""
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        if not self.head:  # List is empty
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            # Traverse to the last node
            while temp.next != self.head:
                temp = temp.next
            # Update links
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        """Delete a node with the given key"""
        if not self.head:  # List is empty
            print("The list is empty. Nothing to delete.")
            return

        # Case 1: Deleting the head node
        if self.head.data == key:
            if self.head.next == self.head:  # Single node case
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
            print(f"Node with data {key} deleted.")
            return

        # Case 2: Deleting other nodes
        current = self.head
        prev = None
        while current.next != self.head:  # Traverse the list
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                print(f"Node with data {key} deleted.")
                return
        print(f"Node with data {key} not found.")

    def search(self, key):
        """Search if a key exists in the list"""
        if not self.head:  # List is empty
            return False

        temp = self.head
        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:  # Came back to the starting point
                break
        return False

    def print_list(self):
        """Print all the elements in the list"""
        if not self.head:  # List is empty
            print("The list is empty.")
            return

        temp = self.head
        print("Circular Linked List elements: ", end="")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Example Usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    # Insert elements
    cll.insert_at_beginning(10)
    cll.insert_at_beginning(20)
    cll.insert_at_beginning(30)
    cll.print_list()  # Output: 30 20 10
    
    # Delete an element
    cll.delete(20)
    cll.print_list()  # Output: 30 10
    
    # Search for elements
    print("Search for 10:", cll.search(10))  # Output: True
    print("Search for 40:", cll.search(40))  # Output: False
    
    # Print the list
    cll.print_list()  # Output: 30 10


# Output:  python CircularLinkedList.py 
# Circular Linked List elements: 30 20 10 
# Node with data 20 deleted.
# Circular Linked List elements: 30 10 
# Search for 10: True
# Search for 40: False
# Circular Linked List elements: 30 10 