
def word_count(words:str):
    arr = words.split()
    return len(arr)


def letter_count(words:str):
    words = words.lower()
    count = {}
    for i in range(0,len(words)):
        letter = words[i]
        if letter not in count:
            count[letter] = 0
        count[letter] += 1
    return count

def convert_dict(count):
    arr = []
    for letter in count:
        arr.append({"char": letter, "num": count[letter]})
    return arr

def sort_on(count):
    return count["num"]