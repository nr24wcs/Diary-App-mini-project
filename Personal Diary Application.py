from datetime import datetime

def write_entry(filename):
    try:
        with open(filename, 'a') as file:
            entry = input("Write your words, and heal your heart: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] {entry}\n")
            print("Yay!! You saved it bestie!!")
    except PermissionError:
        print("Error: Try again my friend! You've got this!!")

def read_entries(filename):
    try:
        with open(filename, 'r') as file:
            entries = file.readlines()
            if entries:
                print("\n--- Your Entries, Your words ---")
                for entry in entries:
                    print(entry.strip())
            else:
                print("\nNo entries found.")
    except FileNotFoundError:
        print("Error: Nothing here Bestie. No entries available.")
    except PermissionError:
        print("Error: Oops! You do not have permission to read this file.")

def main():
    filename = "diary.txt"
    while True:
        print("\nDiary Application")
        print("1. Write a new entry, I love that you're inspired!")
        print("2. View previous entries, re-reading your inspration is GOALS!")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            write_entry(filename)
        elif choice == '2':
            read_entries(filename)
        elif choice == '3':
            print("Bye Bestiiiiieeee!")
            break
        else:
            print("Woopsies, Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
