array = []


def add(item):
    array.append(item)
    print(f"Added {item} at index {len(array) - 1}")


def remove():
    if not array:
        print("Array is empty. Nothing to remove.")
        return
    index = len(array) - 1
    item = array.pop()
    print(f"Removed {item} from index {index}")


def display():
    print("Array:", array if array else "[ ] (empty)")


def main():
    while True:
        print("\n--- ARRAY MENU ---")
        print("1. Add element (end)")
        print("2. Remove element (last index)")
        print("3. Display array")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            item = input("Enter a letter/value to add: ").strip()
            if item:
                add(item)
            else:
                print("Input cannot be empty.")
        elif choice == "2":
            remove()
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