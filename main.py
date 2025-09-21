import sys
from stats import word_count, letter_count, convert_dict, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    words = get_book_text(filepath)
    wcount = word_count(words)
    print("----------- Word Count ----------")
    print(f"Found {wcount} total words")

    lcount = letter_count(words)
    lcountArr = convert_dict(lcount)
    lcountArr.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for entry in lcountArr:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")


main() 