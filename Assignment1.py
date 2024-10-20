# Create a Node class to create a node
class Node:
    def __init__(self, data):  # Corrected method name and indentation
        self.data = data
        self.next = None

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at the beginning of the LinkedList
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at the end of the LinkedList
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Method to get the size of the LinkedList
    def sizeOfLL(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

    # Print method for the LinkedList
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Method to find the middle element of the LinkedList
    def find_middle_element(self, index):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            current_node = current_node.next
            position += 1
        if current_node:
            print(current_node.data)
        else:
            print("Index not present")

# Main function to run the code
def main():
    # Create a new LinkedList
    llist = LinkedList()

    # Add nodes to the LinkedList
    llist.insertAtEnd(1)
    llist.insertAtEnd(2)
    llist.insertAtEnd(3)
    llist.insertAtEnd(4)
    llist.insertAtEnd(5)
    llist.insertAtEnd(6)
    llist.insertAtEnd(7)
    llist.insertAtEnd(8)
    llist.insertAtEnd(9)
    llist.insertAtEnd(10)

    print("Node Data:")
    llist.printLL()

    print("\nMiddle Element of linked list:", end=" ")
    size = llist.sizeOfLL()

    # Find the middle element
    if size % 2 == 0:
        index = size // 2
    else:
        index = (size + 1) // 2

    llist.find_middle_element(index - 1)  # Adjusting index for 0-based indexing

if __name__ == "__main__":
    main()
