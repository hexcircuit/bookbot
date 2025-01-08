def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wc = word_count(text)

    cc = char_count(text)

    output = report(cc)

    print(f"--- Begin report of {book_path} ---")
    print(f"{wc} words found in the document")
    print()

    # Print the output line by line
    for line in output:
        print(line)
    
    print("--- End report ---")


# a function that reads a file and returns the text as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()


# a function that counts the number of words in a text
def word_count(text):
    words = text.split()
    return len(words)


# a function that counts the number of characters in a text and stores in a dictionary
def char_count(text):
    low_text = text.lower()
    counts = {}
    for char in low_text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts


# a function that sorts and formats the character counts
def report(dict):
    def sort_on(item):
        return item["count"]

    dict_list = [{"char": char, "count": count} for char, count in dict.items()]  # converts dictionary to list of dictionaries
    sorted_list = sorted(dict_list, reverse=True, key=sort_on)  # sorts the list of dictionaries

    output = []
    for item in sorted_list:
        output.append(f"The letter '{item['char']}' appears {item['count']} times in the text")
    
    return output  # Return the list of formatted strings


main()
