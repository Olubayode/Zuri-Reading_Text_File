import os
import string
file_path = 'C:/Users/OLUBAYODE/Downloads/Reading-Text-Files/story.txt'
filename = os.path.dirname(file_path)
# print(filename)

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    # f = open(Path.cwd()/'newfile.txt', 'rt')
    
    file = open(filename, 'rt')
    text = file.read()#.replace('\n', ' ')
    # print(text)
    file.close()
    return text


read_file_content(file_path)

def count_words():
    text = read_file_content("C:/Users/OLUBAYODE/Downloads/Reading-Text-Files/story.txt")
    print(text)
    # [assignment] Add your code here
    text = text.split() # Split th line into words 
    dict_ = dict() # Create an empty dictionary
    
    for w in text:
        word = w.lower().replace('.', '') # convert the characters in line(word) to lowercase to avoid case mixmatch and replace punctionation (.) with empty string
        word = w.lower().replace('?', '') 
        if word.lower() in dict_:# check if the word is already in dictionary 
            dict_[word] = dict_[word] + 1 # increment count of word by 1 
        else:
            dict_[word] = 1 #Add the word to dictionary with count 1 
    for key in list(dict_.keys()): # Print all the contennts of the dictionary
        # print(key, ":", dict_[key])
        return 
        
count_words()

