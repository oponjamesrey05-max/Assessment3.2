from collections import deque

queue = deque()


def enqueue(item):
    queue.append(item)
    print(f"append({item})")


def dequeue():
    if not queue:
        print("Queue is empty. Nothing to remove.")
        return
    print(f"popleft -> removes {queue.popleft()}")


def display():
    print("Queue (front to back):", ", ".join(queue) if queue else "empty")


def main():
    while True:
        print("\n--- QUEUE MENU (FIFO) ---")
        print("1. append (enqueue)")
        print("2. popleft (dequeue)")
        print("3. Display queue")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            item = input("Enter a letter/value to add: ").strip()
            if item:
                enqueue(item)
            else:
                print("Input cannot be empty.")
        elif choice == "2":
            dequeue()
        elif choice == "3":
            pass
        elif choice == "4":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Try again.")
            continue
        display()


if __name__ == "__main__":
    main()