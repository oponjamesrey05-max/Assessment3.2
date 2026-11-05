class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node(data)
        if self.tail is None:  # first node: head and tail
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # old tail points forward
            new_node.prev = self.tail  # new node points back
            self.tail = new_node
        print(f"Added node {data}")

    def remove_tail(self):
        if self.tail is None:
            print("List is empty. Nothing to remove.")
            return
        removed = self.tail.data
        if self.head is self.tail:  # only one node left
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev  # move tail back
            self.tail.next = None
        print(f"Removed tail {removed}")

    def display(self):
        if self.head is None:
            print("List: empty")
            return
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        print("List: " + " <-> ".join(parts))


def main():
    lst = DoublyLinkedList()
    while True:
        print("\n--- DOUBLY LINKED LIST MENU ---")
        print("1. Add node (tail)")
        print("2. Remove tail node")
        print("3. Display list")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            item = input("Enter a letter/value to add: ").strip()
            if item:
                lst.add(item)
            else:
                print("Input cannot be empty.")
        elif choice == "2":
            lst.remove_tail()
        elif choice == "3":
            pass
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")
            continue
        lst.display()


if __name__ == "__main__":
    main()