
############################################################################
## This script will take in a group of .txt files from a folder and spit out
## an equal number of fully formated HTML files.
############################################################################
## Unimplemented features list
##
## * Make outputted HTML files have the names of their blog post title
## * Create a css document for the html
## * Dynamicly create an index.html file
## * Create option to upload to test/live server
############################################################################

import os

#########################################################################
## Create a list of the text files to be read and format it to remove any
## items containing "._"
#########################################################################

blog_posts = os.listdir(os.getcwd() + "/blogposts")

blog_posts_formated = []

for i in blog_posts:
    if not i.startswith("._"):
        blog_posts_formated.append(i)

## Create a list of all the content to be applied to each webpage

blog_posts_content = []

for i in blog_posts_formated:
    temp = open(os.getcwd() + "/blogposts/" + i)
    temp2 = temp.read()
    blog_posts_content.append(temp2)

    
########################################################################
## Create a list of urls from the titles of the text documents
## accsessed and formated above. These will make our blog post list.
########################################################################

blog_posts_nav = blog_posts_formated
blog_posts_nav_clean = []
blog_posts_nav_html = []
blog_posts_nav_nws = []
blog_posts_nav_lower = []
nav_list = []
nav_list_link = []
nav_list_title = []


# 1. Remove the .txt suffixes (MAKE THIS A FUNCTION)
for h in blog_posts_nav:
    h = h[:-4]
    blog_posts_nav_clean.append(h) # Use this one for showing names

# 2. Add the .html suffix
for h in blog_posts_nav_clean: 
    h = h + ".html"
    blog_posts_nav_html.append(h)

# 3. Remove whitespaces and make lowercase  
for h in blog_posts_nav_html:
    h = h.replace(" ", "_")
    blog_posts_nav_nws.append(h)

for h in blog_posts_nav_nws:
    h = h.lower()
    blog_posts_nav_lower.append(h)
    
# 4. Create a list of html strings, and iterate through them, replacing with
#    content from our created lists.
for h in [x for x in range(len(blog_posts_nav_lower))]:
    nav_list.append('<li><a href="BLOG LINK">BLOG TITLE</a></li>')
    
for h in [x for x in range(len(blog_posts_nav_lower))]:
    temp = nav_list[h].replace("BLOG LINK", blog_posts_nav_lower[h])
    nav_list_link.append(temp)

for h in [x for x in range(len(blog_posts_nav_lower))]:
    temp = nav_list_link[h].replace("BLOG TITLE", blog_posts_nav_clean[h])
    nav_list_title.append(temp)
    
# 5. Create an full HTML string by concatonating the final list  
nav_list_final = "<ul>" + "</n>".join(nav_list_title) + "</ul>"

##########################################################################    
## Using our formated html to creating a list of HTML strings, one
## for each page. These will be our blog post bodies.
##########################################################################

html_list1 = []
html_list2 = []
html_list3 = []

# Get and read the html from our template.html file
html_part = open(os.getcwd() + "/template.html")
html_part = html_part.read()

# Replace the REPLACE BODY tag with body html
for i in blog_posts_content: 
    temp3 = html_part.replace("REPLACE BODY", i)
    html_list1.append(temp3)

# Replace the REPLACE LINKS tag with our final link html code
for i in html_list1:
    temp4 = i.replace("REPLACE LINKS", nav_list_final)
    html_list2.append(temp4)

# Replace the REPLACE TITLE tag with our blog page title
for i in range(len(html_list2)):
    temp5 = html_list2[i].replace("REPLACE TITLE", blog_posts_nav_clean[i])
    html_list3.append(temp5)

############################################################################
## For each item in the list created in the above step, write an HTML file
## containing the item in a seperate folder.
############################################################################

num = 0

for i in html_list3:
    num += 1
    with open(os.getcwd() + "/html/" + "test" + str(num) + ".html", "w") as temp:
        temp.write(i)
