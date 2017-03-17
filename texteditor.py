import os
#tells python to use the module 'os' 

os.chdir("/Users/yosemite/Documents/textswappingwork/")
#changes to a particular directory
#Todo: edit this so the program can be called anywhere

#file1 = str(input('which file?'))
file1 = "read.txt"
#asks user this question, takes input and assigns it to the string variable 'file1'

#Todo: have it ask which *file* to go to for the list of substitutions ... even better, allow going through folder tree
#Or even better run this with parameters in commandline ... 
#... >python texteditor.py oldfilename newfilename substitutionlistfilename (+ other parameter perhaps) 

Old1 = str(input('What is your old word?'))
New1 = str(input('What is your new word?'))
Old2 = str(input('What is your old word?'))
New2 = str(input('What is your new word?'))
  
thefile = open(file1,'r')
#opens file1, read mode

content = thefile.read()
#copies everything in the file and assigns it to the string variable content

content = content.replace(Old1 ,New1)
content = content.replace(Old2 ,New2)
#makes requested substitutions

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