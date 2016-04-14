textfile = open('C:/Users/Alex/Desktop/Scrabbledictionary.txt', 'r')  # Opening the textfile which contains all the words accepted in scrabble
wordlist = textfile.read()  # Read the words into a list
words = wordlist.split('\n')  # Split the list into row form

value_list = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
              'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
              'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
              'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

letters = input("Write your seven letters here, in form ['a', 'b',...] ->")  
#letters = ['a','u','c','d','e','f','g','h']

def wordgenerator(L):
    """
    A function to determine whether all seven letters in the list can form a valid word
    """
    valid = []  # Set up a starting list
    scores = []
    for row in words:  # Check each row for the first letter
        if all(True if row.count(item) <= L.count(item) else False for item in row): # Counts the number of each letter in the word and checks if there is the same number or less in the list of letters
            valid.append(row)  # Append each valid word into the list
    return valid

def find_value(word):
    return sum(value_list[char] for char in word)

w = wordgenerator(letters)

for e in w:
    #string = "If you play %s, you will score %i points" % (e, find_value(e))
    #print string
    print e,'', find_value(e)
