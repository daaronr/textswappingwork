#texteditor.py
#Description: uses csv-format file 'dictionary' to make a series of replacements in 'oldfile' and create 'newfile'
#Execute as "python texteditor.py oldfile dictionary"
#Creates 'newfile'
#see also README.md

import os
#tells python to use the module 'os'

import sys
#tells python to use the module 'sys' used to do one line command in the terminal


#changes to a particular directory
#Todo: edit this so the program can be called anywhere, look for files in the given directory or based on input

arglist = sys.argv
#creates a list which stores the variables which are input directly in the one-line command in the terminal

oldfile = str(arglist[1])
newfile = str(arglist[2])
dic = str(arglist[3])
colonne = int(arglist[4])
chosenDirectory = str(arglist[5])
#takes as variable the elements of list 'arglist'
    #Todo: default 'newfile=oldfile' if no third argument
os.chdir(chosenDirectory)
#Run this with parameters in commandline ... python texteditor1.py oldfilename newfilename substitutionlistfilename columnNumberinCSV directoryofNewfile(+ other parameter perhaps)

mydictionary = open(dic,'rb')
data = csv.reader(mydictionnary)
d={}
# creates a dictionary called d
colonne = colonne - 1

for line in mydictionary:
    x=line.split(',')
    a = x[0]
    b = x[colonne]
    for p in b:
        b = b.replace('+' ,',')
#no presentation errors eg. new line or extra spaces
    #DR: Later on we may want to allow quoted strings containing characters like newline
    #DR: I'm not sure if we want this 'cleanup' -- is it necessary?
    #DR: Also, we need a way to allow *intended* commas in the dictionary file itself; perhaps "\," suffices

    d[a]=b
# x is a string which contains the whole line
# x[0] is the first word of the line x[1] is the second
# d[a]=b appends in the dictionary (d) the old and new word in the form d{'oldword' = newword}

mydictionary.close()

thefile = open(oldfile,'r')
#opens oldfile, read mode

content = thefile.read()
#copies everything in the file and assigns it to the string variable 'content'

for k, v in d.items():
    content = content.replace(k ,v)
#makes requested substitutions using the dictionary d
   #DR: How does this command work? Also, why did you choose the letters 'k' and 'v'

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
mynewfile = open(newfile,'w+')
#mynewfile = open("newfile.txt",'w+')
    #DR: can we have this file named based on the third input argument?
mynewfile.write(content)
mynewfile.close()
