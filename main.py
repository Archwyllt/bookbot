def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def number_length(book_str):
    return len(book_str.split())

def char_count(book_str):
    count = {}

    for char in book_str.lower():
        if char in count:
            count[char] += 1
        else: 
            count[char] = 1
    return count

def report(book_str, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_length(book_str)} words found in the document\n")

    for letter in "abcdefghijklmnopqrstuvwxz":
        print(f"The '{letter}' character was found {char_count[letter]} times")
    
    print("--- End report ---")

if __name__ == "__main__":
    report(main(), char_count(main()))