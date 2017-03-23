import os
#tells python to use the module 'os'

import sys
#tells python to use the module 'sys' used to do one line command in the terminal

os.chdir("/Users/yosemite/Documents/textswappingwork/")
#changes to a particular directory
#Todo: edit this so the program can be called anywhere

arglist = sys.argv
#creates a list which stores the variables which are inputed directly in the one line command in the terminal

file1 = str(arglist[1])
file2 = str(arglist[2])
#takes as variable the elements of list 'arglist'

#Run this with parameters in commandline ... python texteditor.py oldfilename newfilename substitutionlistfilename (+ other parameter perhaps)

mydictionary = open(file2,'r')
d={}
# creates a dictionary called d

for line in mydictionary:
    x=line.split(',')
    a = x[0]
    b = x[1].strip()
#no presentation errors eg. new line or extra spaces
    #DR: Later on we may want to allow quoted strings containing characters like newline

    d[a]=b
    # x is a string which contains the whole line
    # x[0] is the first word of the line x[1] is the second
    # d[a]=b appends in the dictionary (d) the old and new word in the form d{'oldword' = newword}

mydictionary.close()

thefile = open(file1,'r')
#opens file1, read mode

content = thefile.read()
#copies everything in the file and assigns it to the string variable content

for k, v in d.items():
    content = content.replace(k ,v)

#makes requested substitutions using the dictionary d

#to change the existing file this is the code :
    #DR: For future work, let's allow a parameter to the command that specifies whether it edits in place or creates a new file;
    #... or even better, have it edit in place if the new and old filenames and locations are identical

'''
thefile.close()
#closes the file to allow edits
thefile = open(file1,'w')
#opens the file in the writing mode
thefile.truncate()
#clears all text from thefile
thefile.write(content)
#puts in the text from the string variable 'content'
thefile.close()
#need to close the file for some reason
'''

#to create a new file this is the code:
mynewfile = open("newfile.txt",'w+')
mynewfile.write(content)
mynewfile.close()
