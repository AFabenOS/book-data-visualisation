# Project Outline

## What is this project about?

This project will build upon and fix my original program that intended on
parsing html files from Project Gutenberg, a website that stores books that are
in the public domain. 

The first stage of the project involves cleaning up the parsed text:
- The parsed files will then be cleaned up to contain only the book's text and
remove additional information (such as copyright, legal notices, Project
Gutenberg information, etc.).
- Following this the text will then be examined to remove any floating pieces
of text that the html parser missed after which the "pure" text will then be
split and joined to ensure each word is spelled correctly and not accidentally
joined with another word ("freenorth" would become "free" and "north"
as an example).
- Finally all the words will be converted to lower case to ensure
each word is identical (e.g. "Deer" != "deer").

The second stage of the project involves analysing these files and will look
at:
- Word counts
- Number of unique words in the text
- Most common words
- Least common words

## Who is this project made for?

- This project is designed primarily for me as a learning experience, but would
also be useful to others seeking various information from certain books.
- The project will also be available to other budding programmers to see how a 
beginner programmer produces their code.


## What will I learn from completing this project?
- This project will reinforce core Python concepts such as OOP and functions
- The project involves some minor RegEx understanding
- HTML parsing is something I'm not familiar with and working with the 
BeautifulSoup module will help with learning how to use this effectively
- Data visualisation using matplotlib is something I've used before, but will 
be great to experiment with to present data in better and clearer ways for
people wishing to look at the data.
- The project will be made with a TDD mindset (test first approach)
