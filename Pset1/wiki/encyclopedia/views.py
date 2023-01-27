import random

from django.shortcuts import render

from . import util


# Convert Markdown markup language to HTML before display back to user. Install via command: pip3 install markdown2
from markdown2 import Markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Define a function to convert Markdown format of input title to output corresponding content in HTML format
def conversion(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    # Evaluate and return converted text contents if input text found within entries
    if content == None:
        return None
    else:
        return markdowner.convert(content)

# Get a string of title from URL path
def entry(request, title):
    entry_content = conversion(title)
    # Evaluate and return title and content of entry if exist else return error message
    if entry_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Page Not Found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": entry_content
        })

# Search for the entry based on user query in search box in sidebar
def search(request):
    if request.method == "POST":
        # Obtain data from form
        usr_search = request.POST['q']
        search_content = conversion(usr_search)
        if search_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": usr_search,
                "content": search_content
            })
        else:
            # Evaluate if input is substring of one of the entries and update list and render display if true
            entries = util.list_entries()
            search_recommendations=[]
            for entry in entries:
                if usr_search.lower() in entry.lower():
                    search_recommendations.append(entry)
            return render(request, "encyclopedia/search.html", {
                "search": search_recommendations
            })

# Add new entry to Wiki
def new_page(request):
    # User submit request via GET(Request for page)
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    # User submits request via POST(Submit data via form or button)
    else:
        new_title = request.POST["newpage_title"]
        new_text = request.POST["newpage_txt"]
        title_exist = util.get_entry(new_title)
        # Evaluate if input title matches with existing entries
        if title_exist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry Already Exists"
            })
        else:
            # Save input into entries list and convert Markdown content to HTML format
            util.save_entry(new_title, new_text)
            new_content = conversion(new_title)
            return render(request, "encyclopedia/entry.html", {
                "title": new_title,
                "content": new_content
            })

# Add edit content option for each display entry. Preloaded corresponding entry content in edit html page for editing.
def edit(request):
    if request.method == "POST":
        title = request.POST["edit_title"]
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })

# Save edits and reroute user to corresponding entry page
def save_edit(request):
    if request.method == "POST":
        title = request.POST["editpage_title"]
        content = request.POST["editpage_txt"]
        util.save_entry(title, content)
        latest_html = conversion(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": latest_html
        })

# Return random entry from list of entries. If local files have name as random, attribute error choice not found in random will occur since shadowed by local file.
def rand(request):
    all_entries = util.list_entries()
    rand_entry = random.choice(all_entries)
    convert_rand = conversion(rand_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rand_entry,
        "content": convert_rand
    })
