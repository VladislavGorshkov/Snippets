from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    #Создаем пустую форму при запросе методом GET
    if request.method =="GET":
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
               'form':form,
               }
        return render(request, 'pages/add_snippet.html', context)
    #Получаем данные из формы и на их основе создаем новый экземпляр
    if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("snippets_page")
    return render(request,'add_snippet.html',{'form': form})

def snippets_page(request):
    snippets = Snippet.objects.all()
    context={'pagename': 'Просмотр сниппетов',
            "snippets":snippets}
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request,snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Snippet{snippet_id} not fount")
    context={'pagename': 'Просмотр сниппетов',
            "snippet":snippet,}

    return render(request, 'pages/snippet_detail.html', context)

# def create_snippet(request):
#    if request.method == "POST":
#        form = SnippetForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect("snippets_page")
#        return render(request,'add_snippet.html',{'form': form})

def del_snippet_page(request, snippet_id):
       snippet = Snippet.objects.get(id=snippet_id)
       snippet.delete()
       return redirect("snippets_page")
    
def edit_snippet_page(request, snippet_id):
    if request.method =="GET":
        try:
            snippet = Snippet.objects.get(id=snippet_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound(f"Snippet{snippet_id} not fount")
        context={'pagename': 'Просмотр сниппетов',
            "snippet":snippet,}

        return render(request, 'pages/red_snippet.html', context)
     #Создаем пустую форму при запросе методом GET
    #if request.method =="GET":
        #form = SnippetForm()
    #     context = {'pagename': 'Редкатирование сниппета',
    #            'snippet':snippet,
    #            }
    # return render(request, 'pages/red_snippet.html', context)
    #Получаем данные из формы и на их основе создаем новый экземпляр
    if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
            snippet.name="New name" #request.POST("name")
            snippet.save()
            return redirect("snippets_page")
    return redirect("snippets_page")


