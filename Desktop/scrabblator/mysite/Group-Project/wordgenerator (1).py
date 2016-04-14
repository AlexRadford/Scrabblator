textfile = open('ScrabbleDictionary.txt', 'r')  # Opening the textfile which contains all the words accepted in scrabble
wordlist = textfile.read()  # Read the words into a list
words = wordlist.split('\n')  # Split the list into row form

letters = ['j', 'u', 'k', 'e', 'b', 'o', 'x']  # Sample list of letters

def wordgenerator(L):
    """
    A function to determine whether all seven letters in the list can form a valid word
    """
    valid1 = []  # Set up a starting list
    for row in words:  # Check each row for the first letter
        print row
        if all(True if row.count(item) <= L.count(item) else False for item in row):  #does a thing that works O.o
            valid1.append(row)  # Append each valid seven letter word into the list
    return valid1

wordgenerator(letters)
wordgenerator(['c', 'a', 't', 'k'])











