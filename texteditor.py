import os

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
