
import sys, string


def to_lower(words):
    wordList = list() #creates empty list
    for word in words: #for each word in words, take every element and convert to lowercase
        wordList.append(word.lower())
    return wordList

def remove_punc(words):
    wordList = list()
    for word in words: #for each word in words, remove punctuation marks and non alphanumeric letters 
        tempWord = ""
        for letter in word:
            if letter in string.ascii_letters or letter in string.digits:
                tempWord += letter
        wordList.append(tempWord)
    return wordList
        
def remove_digits(words):
    wordList = list()
    for word in words: #removes elements that have both letters and numbers 
        cumlative_word = ""
        for letter in word:
            if letter not in string.digits:
                cumlative_word += letter
        if cumlative_word == "":
            wordList.append(word) #because the word is a number fully.
        else:
            wordList.append(cumlative_word)
    return wordList

def remove_stop_words(words):
    wordList = list()
    for word in words: #removes any word in Stop_Words array
        if not word in Stop_Words:
            wordList.append(word)
    return wordList

def processed_words(words):
    processed = list()
    for word in words: #removes empty elements from string arrays
        if not word == "" and not word in processed:
            processed.append(word)
    return processed

# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
    ]

if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    inputs = sys.argv
    mod = ""
    if len(inputs) >= 2:
        if inputs[1] in ["keep-digits", "keep-stops", "keep-symbols"]:
            mod = inputs[1]
        else:
            print("Entered mode values are invalid.")
            print("Please use python3 preprocess.py <modes>")
            print("Acceptable modes are: keep-digits, keep-stops, keep-symbols")
            exit(1)
    words = input().split()
    lowercase = to_lower(words)
    words = lowercase

    if mod == "keep-symbols":
        words = remove_digits(words)
        words = remove_stop_words(words)

    if mod == "keep-digits":
        words = remove_punc(words)
        words = remove_stop_words(words)

    if mod == "keep-stops":
        words = remove_punc(words)
        words = remove_digits(words)
    
    if not mod:
        words = remove_punc(words)
        words = remove_digits(words)
        words = remove_stop_words(words)
    processed_words = processed_words(words)
    print(*processed_words) 
pass
