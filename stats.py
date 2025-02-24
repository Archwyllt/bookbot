def get_num_words(book_str):
    return len(book_str.split())

def char_count(book_str):
    count = {}

    for char in book_str.lower():
        if char in count:
            count[char] += 1
        else: 
            count[char] = 1
    return count

def sorted_list(char_counts):
    result = []
    
    for char, count in char_counts.items():
        char_dict = {char: count}
        
        result.append(char_dict)

    result.sort(key=lambda x: list(x.values())[0], reverse=True)
    
    return result