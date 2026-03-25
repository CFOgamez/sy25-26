import datetime

def write_submission():
    entry = input("write your diary submission: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_entry = f"{timestamp}\n{entry}\n{'-'*40}\n"
    with open("my_diary.txt", "a") as file:
        file.write(formatted_entry)
    print(f"submission saved ({len(entry)} characters)")

def read_submission():
    try:
        with open("my_diary.txt", "r") as file:
            entries = file.read()
            if entries.strip():
                print("Your diary submission:\n")
                print(entries)
            else:
                print("Your diary has nothing in it.")
    except FileNotFoundError:
        print("Your diary has nothing in it. no submission found")

def refreshed_diary():
    with open("my_diary.txt", "w") as file:
        pass  
    print("Diary refreshed. You can start a new page")

def main():
    while True:
        print("welcome to the diary menu, choose one option (1, 2, 3, or 4)?")
        print("1. write, 2. read, 3. clear,4. exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            write_submission()
        elif choice == '2':
            read_submission()
        elif choice == '3':
            refreshed_diary()
        elif choice == '4':
            print("goodbye.")
            break
        else:
            print("invalid option.")


main()

