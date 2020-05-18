from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index_in_view(request):
    articles_movie_count = Article.objects.filter(category="movie").count()
    articles_drama_count = Article.objects.filter(category="drama").count()
    articles_entertain_count = Article.objects.filter(category="entertain").count()
    return render(request, 'index.html', {
        'articles_movie_count':articles_movie_count,
        'articles_drama_count':articles_drama_count,
        'articles_entertain_count':articles_entertain_count
    })
    

def movie_in_view(request):
    articles_movie = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'articles_movie':articles_movie})

def drama_in_view(request):
    articles_drama = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'articles_drama':articles_drama})

def entertain_in_view(request):
    articles_entertain = Article.objects.filter(category="entertain")
    return render(request, 'entertain.html', {'articles_entertain':articles_entertain})

def new_in_view(request):
    if request.method == "POST":
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = request.POST['time']
        )
        return redirect('detail_html',primary_articles=new_article.pk)
    else:
        return render(request, 'new.html')

def detail_in_view(request, primary_articles):
    article = Article.objects.get(pk=primary_articles)
    return render(request, 'detail.html', {'article':article})