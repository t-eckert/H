# Compile to README
from glob import glob

DIRLIST = glob('/Users/t-eckert/Documents/Work/H/*/')
CHAPTERS = []

for directory in DIRLIST:
    directory = directory.split('/')[-2]
    CHAPTERS.append(directory)

README = open('README.md','w')
OUTPUT = ''

def write_toc(chapters):
    str_out = '# Table of Contents \n\n'
    for chapter in chapters:
        tag = chapter.split(':')[0].replace(' ','-')
        str_out += '- [' +chapter +'](#' +tag +')  \n'
    str_out += '\n'
    return str_out

def dir_to_markdown(chapter):
    '''Returns a chapter in Markdown format.'''
    main = open(chapter +'/main.txt')
    tag = chapter.split(':')[0].replace(' ','-')
    anchor = '<a name="' +tag +'"></a>'
    formatted_ch = '\n\n### ' +anchor +chapter.split(':')[0] 
    formatted_ch += '\n##' +chapter.split(':')[1]
    for line in main:
        if '***' not in line: 
            formatted_ch += '\n' +line
    # Need to figure out how to handle images and equations when the time comes
    return formatted_ch

README.write('# Exploring the Universe Through Hydrogen: A Beginners Guide to Physics\n')
README.write('![Hydrogen Cover](HydrogenCover.png) \n')
README.write(write_toc(CHAPTERS))

for chapter in CHAPTERS:
    OUTPUT += dir_to_markdown(chapter)

README.write(OUTPUT)