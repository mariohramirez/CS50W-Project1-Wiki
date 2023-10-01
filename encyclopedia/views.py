from django.shortcuts import render
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, title):
    #We get the content from the entry given a title
    content = util.get_entry(title)

    #We verify if the content has something in it
    if content:
        return render(request, "encyclopedia/entry.html", {
            "entryName": title, "content": markdown2.markdown(content)
        })
    #If the content is empty
    else:
        return render(request, "encyclopedia/error.html")

