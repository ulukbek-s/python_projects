from django.shortcuts import render
from PyDictionary import PyDictionary
# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    context = {
        'meaning': meaning,
    }
    return render(request, 'word.html', context)