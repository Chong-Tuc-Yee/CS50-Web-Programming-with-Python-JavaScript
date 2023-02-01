### Task: ### 
**Design a Wikipedia-like online encyclopedia.**

### Specification: ###
Framework: **Django** <br>
Language: **Python, HTML, CSS, Markdown**

**Website Function:**

Enables user to visit encyclopedia page, create a new entry, edit the entry, query for a specific encyclopedia entry through search box and enable user to search for a random encyclopedia entry.

**Website Requirement:**

Practice Question Source: [More Info](https://cs50.harvard.edu/web/2020/projects/1/wiki/)

### Usage: ###
User need to download Django to run this program via this command: `pip3 install Django`

Each encyclopedia entry is keyed in by user and saved in Markdown format and will be converted to HTML format before being displayed back to user. <br>
User may use the [`python-markdown2`](https://github.com/trentm/python-markdown2) package to perform this conversion, installable via command: `pip3 install markdown2`

To run this program, user can execute following commands in codespace terminal window after installing the packages mentioned above:
1. `cd Pset1`
2. `cd wiki`
3. `python manage.py runserver`

Since Django uses token to prevent CSRF attack, if below error message pops out upon submitting request, please copy your website link shown in error message and paste it over to `settings.py` file inside main folder with this line of code: `CSRF_TRUSTED_ORIGIN = ['url']` where url is the link you copied.
![image](https://user-images.githubusercontent.com/107826905/215513882-bcfe505c-005e-4cb8-8c28-c6df33525c5d.png)
![image](https://user-images.githubusercontent.com/107826905/215512114-baf43687-3874-41a6-80aa-72ab19b4e567.png)

### Program Example: ###
**Main Page / Index Page**
![image](https://user-images.githubusercontent.com/107826905/215511284-d500193b-cffe-42f9-92f5-556bbe53b8e1.png)

**Create New Page (Create New Encyclopedia Entry)**
![image](https://user-images.githubusercontent.com/107826905/215511386-7f84760d-9aa9-4f95-9559-5cb1c75f7b0b.png)

**Search Function (Type Query Into Search Box At Sidebar, Display all Results that Have Query As Substring)** <br>
*Query Example*
![image](https://user-images.githubusercontent.com/107826905/215512536-8b5845c8-78f4-4241-a84f-de62ea05b5b6.png)

*Result*
![image](https://user-images.githubusercontent.com/107826905/215512621-66475f31-1aef-4d45-bb20-65c0e1699f21.png)

**Entry Page (Display contents of a particular encyclopedia entry)**
![image](https://user-images.githubusercontent.com/107826905/215512742-ac586d8d-c0c0-4bc5-b361-d9c212ee13e2.png)

**Edit Page (Edit Entry Content)**
![image](https://user-images.githubusercontent.com/107826905/215512975-400adece-4f85-4fb6-b11a-0e4658d4916c.png)



