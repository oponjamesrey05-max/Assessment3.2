stack = []

def push(item):
    stack.append(item)
    print(f"append({item})")


def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
        return
    print(f"pop -> removes {stack.pop()}")


def display():
    print("Stack (bottom to top):", ", ".join(stack) if stack else "empty")


def main():
    while True:
        print("\n--- STACK MENU (LIFO) ---")
        print("1. append (push)")
        print("2. pop")
        print("3. Display stack")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            item = input("Enter a letter/value to push: ").strip()
            if item:
                push(item)
            else:
                print("Input cannot be empty.")
        elif choice == "2":
            pop()
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