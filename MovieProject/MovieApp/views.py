from django.shortcuts import render
from MovieApp.models import Movies
from MovieApp.forms import MoviesForm
# Create your views here.

def add_movie_view(request):
    formObj=MoviesForm()
    if request.method=='POST':
        formObj=MoviesForm(request.POST)
        if formObj.is_valid():
            print(formObj.cleaned_data['releasedate'])
            print(formObj.cleaned_data['moviename'])
            print(formObj.cleaned_data['actor'])
            print(formObj.cleaned_data['actress'])
            print(formObj.cleaned_data['rating'])
            formObj.save()  # auto-commit
           # return index_view(request)
    return render(request, 'MovieApp/addmovie.html', {'form1': formObj})

def index_view(request):
    return render(request, 'MovieApp/index.html');
def list_movie_view(request):
 movies_list=Movies.objects.all().order_by('-rating') #(-)desc-order
 return render(request,'MovieApp/listmovie.html',{'movies_list':movies_list})

