#PyBloggish
==========

PyBloggish is a breakable toy that allows me to maintain a light and simple blog with just a folder of text files

###How to Install and Run

1. Clone to local computer.
2. Put blog posts, in .txt format, into folder "blog posts"; file names will become blog titles.
3. Run txttohtml.py
4. for each .txt, script will output a .html, which will be placed into folder "html"

####How to config

program uses template.html to create its outputed html files. 

* The tag "REPLACE BODY" is where the blog post content will go. 
* The tag "REPLACE LINKS" is where the blog post list will go. 
* The tag "REPLACE TITLE" is where the blog post title will go.

###Project History

###Project Philosophy

###Features to implement
* Make outputted HTML files have the names of their blog post titles
* Create a css document for the html template
* Dynamicly create an index.html file
* Create option to upload to test/live server
