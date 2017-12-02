# Compile to README
from glob import glob

DIRLIST = glob('/Users/t-eckert/Documents/Work/H/*/')
CHAPTERS = []

for directory in DIRLIST:
    directory = directory.split('/')[-2]
    CHAPTERS.append(directory)

README = open('README.md','w')
OUTPUT = ''

def dir_to_markdown(chapter):
    '''Returns a chapter in Markdown format.'''
    main = open(chapter +'/main.txt')
    formatted_ch = '\n\n### ' +chapter.split(':')[0]
    formatted_ch += '\n#' +chapter.split(':')[1]
    for line in main:
        if '***' not in line: 
            formatted_ch += '\n' +line
    # Need to figure out how to handle images and equations when the time comes
    return formatted_ch

for chapter in CHAPTERS:
    OUTPUT += dir_to_markdown(chapter)

README.write(OUTPUT)