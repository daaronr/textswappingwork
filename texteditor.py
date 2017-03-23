import os
<<<<<<< HEAD

os.chdir("/Users/davidserero/Documents/")

file1 = str(input('which file?'))
Old1 = str(input('What is your old word?'))
New1 = str(input('What is your new word?'))
Old2 = str(input('What is your old word?'))
New2 = str(input('What is your new word?'))

infile = open(file1,'r')
content = ''
content = infile.read()
content = content.replace(Old1 ,New1)
content = content.replace(Old2 ,New2)
infile.close()

infile = open(file1,'w')
infile.truncate()
infile.write(content)
infile.close()

#dr edits
=======
#tells python to use the module 'os' 

os.chdir("/Users/yosemite/Documents/textswappingwork/")
#changes to a particular directory
#Todo: edit this so the program can be called anywhere

#file1 = "read.txt"
file1 = str(input('which file?'))
#asks user this question, takes input and assigns it to the string variable 'file1'
file2 = str(input('what is the name of the dictionnay?'))

#Todo: have it ask which *file* to go to for the list of substitutions ... even better, allow going through folder tree
#Or even better run this with parameters in commandline ... 
#... >python texteditor.py oldfilename newfilename substitutionlistfilename (+ other parameter perhaps) 

mydictionnary = open(file2,'r')
d={}
# creates a dictionnary called d
for line in mydictionnary:
    x=line.split(',')
    a = x[0]
    b = x[1]
    d[a]=b
    # x is a string which contains the whole line
    # x[0] is the first word of the line x[1] is the second
    # d[a]=b appends in the dictionnary (d) the old and new word in the form d{'oldword' = newword}
mydictionnary.close()

thefile = open(file1,'r')
#opens file1, read mode

content = thefile.read()
#copies everything in the file and assigns it to the string variable content

for k, v in d.items():
    content = content.replace(k ,v)
#makes requested substitutions using the dictionnary d

#to change the existing file this is the code :
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

#to create a new file this is the code :
mynewfile = open("newfile.txt",'w+')
mynewfile.write(content)
mynewfile.close()

>>>>>>> parent of e9f7460... Update texteditor.py
