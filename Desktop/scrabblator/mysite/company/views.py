from django.shortcuts import render
from calculator import views

from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext
from django import forms

def index(request):
    return render(request, 'company/home.html')

def contact(request):
    return render(request, 'company/basic.html')

    
def buttonClickScript(request):
    # getting input letters
    letter1 = request.GET['T1']
    letter2 = request.GET['T2']
    letter3 = request.GET['T3']
    letter4 = request.GET['T4']
    letter5 = request.GET['T5']
    letter6 = request.GET['T6']
    letter7 = request.GET['T7']
    letter8 = request.GET['T8']
    
    context = {}
    # putting letters back into input fields
    context['value1'] = letter1 
    context['value2'] = letter2
    context['value3'] = letter3
    context['value4'] = letter4
    context['value5'] = letter5
    context['value6'] = letter6
    context['value7'] = letter7
    context['value8'] = letter8

    # START - Modified Code
    textfile = open('C:/Users/Alex/Desktop/scrabblator/mysite/Group-Project/Scrabbledictionary.txt', 'r')  # Opening the textfile which contains all the words accepted in scrabble
    # END - Modified Code
    
    wordlist = textfile.read()  # Read the words into a list
    words = wordlist.split('\n')  # Split the list into row form

    value_list = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
                  'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
                  'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
                  'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

      
    # START - Modified Code
    # This change ensures all letters entered (regardless of input case) are converted to uppercase when searching my uppercase dictionary
    letters = [letter1.lower(),letter2.lower(),letter3.lower(),letter4.lower(),letter5.lower(),letter6.lower(),letter7.lower(),letter8.lower()]
    # END - Modified Code

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
        # START - Modified Code
        # Ensure each letter scored is converted to lowercase (because the value_list is keyed by lower case letters)
        return sum(value_list[char.lower()] for char in word)
        # END - Modified Code

    w = wordgenerator(letters)

    Lws = []

    for i in range(len(w)):
        Lws.append((w[i], find_value(w[i])))

    Sorted_Lws = sorted(Lws, key=lambda word: word[1], reverse = True)
    
    # START - Modified Code
    # Populate table with words found - If there are less words than rows in the table then leave extra rows blank
    # If there are more words than rows in the table, only the top 10 scoring words are displayed
    # Doing it this way means I don't need to work out how to dynamically add/remove rows to the table
    for i in range(10):
        if len(Sorted_Lws) > i :
            # populating first column of table with a word
            context['Word_' + str(i+1)] = Sorted_Lws[i][0]
            # populating second column of table with the score for the word
            context['Score_' + str(i+1)] = Sorted_Lws[i][1]
        else:
            # populating a row of table with blanks (insufficient words to fill table)
            context['Word_' + str(i+1)] = ''
            context['Score_' + str(i+1)] = ''
    # END - Modified Code
    
    template = loader.get_template('company/home.html') # Redraw form
    data = RequestContext(request, context) #with data filled in
    return HttpResponse(template.render(data))
# END - Added Code
