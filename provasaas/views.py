#Qui stiamo creando la view, ovvero la prima pagina web utilizzando python (probabilmente nella mia saas
#utilizzerò react però va beh)tramite la prima riga (from django.http import HttpResponse 
#) importiamo http e tramite la xsfunzione scriviamo nel programma (min 22:00)
import pathlib
from django.shortcuts import render #al posto di usare http response, passiamo render
from django.http import HttpResponse 

from visits.models import PageVisit #obiettivo è di storare i dati raccolti con il visits.models

this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path) #prende all di tutti i dati e ce li mette in tabella
    try:
        percent =  (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": percent,
        "total_visit_count": qs.count()
    }
    path = request.path
    print("path", path)
    html_template = "home.html"
    PageVisit.objects.create(path = request.path)
    return render(request, html_template, my_context)

#copy 

def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_ = """<!DOCTYPE html>
<html>
    <body>
    
        <h1>{page_title}</h1>

    </body>
</html>""".format() #page_title = my_title
    html_file_path = this_dir / "home.html"
    html_ = html_file_path.read_text() #mi da il permesso di leggere il file, aprendo direttamente home.html
    return HttpResponse(html_)