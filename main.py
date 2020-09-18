#David Chetty (CHTDAV009)
#17 May 2016
#Anagram Sets program
""" 
This is a programs that finds all the sets of anagrams of a specified length.
ie. if a length of 4 is specified the the program will search for all anagrams 
of each 4 letter word. 

"""
###############################################################################
"""
The anagramSets() function takes in a word as a parameter and then count
the number of occurences of each letter in the word. Recall that and anagram
is a word that has the same letters in the same quantities.

"""

def anagramSets(w): #function is used inside the main anagram fuction
    
    letter_occurence = {} #creates new dictionary
    
    for letter in w:
        if letter not in letter_occurence:
            letter_occurence[letter] = 1
        else:
            letter_occurence[letter] += 1 
    return letter_occurence  #returns the dictionary with values

"""
The anagrams() function finds all the anagrams of each word in list of words.
 
"""

def anagrams(w,list_words):  #main anagrams function finds the anagrams with equal number of letters and prints them out
    anagramsList = []  #creates an empty list to store the found anagrams
    for items in list_words:
        if anagramSets(items) == anagramSets(w) and items != w: 
            anagramsList.append(items)
    return anagramsList  #returns the list with the anagrams



###############################################################################
"""
Setting up the text based User Interface

"""

text_file = open("EnglishWords.txt", "r")   #opens the file
print("***** Anagram Set Search *****") 
length = eval(input("Enter word length:\n"))
print("Searching...") 
filename = input("Enter file name:\n")
outputFile = open(filename, "w")# open the file in write mode so shat contents can be written to it.
print("Writing results...")


###############################################################################
"""
While loop to skip the copy right part of the file containing the list of
english words. The start of the actual english words is preceeded by the 
word "START" so it is used to terminate the while loop as all information 
after "START" is needed. 
"""

copyright_skip = text_file.readline()    #skips the copy right paragraph
while copyright_skip[:-1] != "START":
    copyright_skip = text_file.readline()


###############################################################################
"""
First find all the words of the specified length and put them in a list because
all anagrams of each of these words will need to be found.   

"""

file_words = text_file.readlines() #reads the rest of the file
text_file.close()    #closes the file
lengthwords = []

"""
For loop to find the words that match the specified length and store them in
a sorted list called lengthwords

"""

for items in file_words:
    items = items[:-1] 
    if len(items) == length:
        lengthwords.append(items)

lengthwords.sort() #sorts the words in alphabetical order
  
"""
For loop to find all the anagrams of each word of the specified length by
invokeing the anagrams() function defined above
"""
 
for things in lengthwords:
    anagram_lst = anagrams(things,lengthwords)
    if anagram_lst:
        anagram_lst.append(things)
        anagram_lst.sort()
        print(anagram_lst, file = outputFile) 
        
        
        for rem in anagram_lst:
            lengthwords.remove(rem)
                      
outputFile.close() #closes the file
print("Finished!")
