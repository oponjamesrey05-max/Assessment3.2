class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"Added node {data}")

    def remove_head(self):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return
        removed = self.head.data
        self.head = self.head.next
        print(f"Removed head {removed}")

    def display(self):
        if self.head is None:
            print("List: empty")
            return
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        print("List: " + " -> ".join(parts) + " -> None")


def main():
    lst = SinglyLinkedList()
    while True:
        print("\n--- SINGLY LINKED LIST MENU ---")
        print("1. Add node (end)")
        print("2. Remove head node")
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
            lst.remove_head()
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