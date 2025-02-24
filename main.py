from stats import get_num_words, char_count, sorted_list
import sys

def main():
    if len(sys.argv) != 2:
        # If not, print usage message and exit with error code
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    pathway = sys.argv[1]
    book_str = get_book_text(pathway)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathway}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_str)} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_list(char_count(book_str)):
        # Each dictionary has one key-value pair
        # Extract the character and count from the dictionary
        char = list(char_dict.keys())[0]
        count = char_dict[char]
        
        # Skip non-alphabetical characters
        if not char.isalpha():
            continue
            
        # Print the character and its count in a formatted string
        print(f"'{char}: {count}")
    
    print("============= END ===============")

def get_book_text(pathway):
    with open(pathway) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()