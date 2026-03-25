def main():
    
    filename = input("Enter file name: ")

    try:

        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found.")
        return

    word = input("Enter word to search: ")

    words = text.lower().split()
    count = words.count(word.lower())

    print(f"The word '{word}' appears {count} time(s).")

if __name__ == "__main__":
    main()
