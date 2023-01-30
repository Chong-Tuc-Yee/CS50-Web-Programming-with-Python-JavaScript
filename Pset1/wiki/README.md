### Task: ### 
**Design a Wikipedia-like online encyclopedia.**

### Specification: ###
Framework: **Django**

**Website Function:**

Enables user to visit encyclopedia page, create a new entry, edit the entry, query for a specific encyclopedia entry through search box and enable user to search for a random encyclopedia entry.

**Website Requirement:**

Practice Question Source: [More Info](https://cs50.harvard.edu/web/2020/projects/1/wiki/)

### Usage: ###
User need to download Django to run this program via this command: `pip3 install django`

Each encyclopedia entry is keyed in by user and saved in Markdown format and will be converted to HTML format before being displayed back to user. <br>
User may use the [`python-markdown2`](https://github.com/trentm/python-markdown2) package to perform this conversion, installable via command: `pip3 install markdown2`

To run this program, user can execute following commands in codespace terminal window after installing the packages mentioned above:
1. `cd Pset1`
2. `cd wiki`
3. `python manage.py runserver`
