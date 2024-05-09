from django.shortcuts import render, redirect
from django.views import View

from moja_muzyka.models import Band, Article


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class BandListView(View):

    def get(self, request):
        bands = Band.objects.all()
        return render(request, 'band_list.html', {'bands': bands})

class AddBandView(View):

    def get(self, request):
        return render(request, 'add_band.html', {'genres':Band.GENRES})

    def post(self, request):
        name = request.POST.get('name')
        year = request.POST.get('year')
        is_active = request.POST.get('is_active') == 'on'
        genre = request.POST.get('genre')
        Band.objects.create(name=name, year=year, still_active=is_active, genre=genre)
        return redirect('band_add')

class UpdateBandView(View):

    def get_object(self, pk):
        return Band.objects.get(pk=pk)

    def get(self, request, pk):
        band = self.get_object(pk)
        return render(request, 'add_band.html', {'genres': Band.GENRES, 'band':band})

    def post(self, request, pk):
        name = request.POST.get('name')
        year = request.POST.get('year')
        is_active = request.POST.get('is_active') == 'on'
        genre = request.POST.get('genre')
        band = self.get_object(pk)
        band.name = name
        band.year = year
        band.still_active = is_active
        band.genre = genre
        band.save()
        return redirect('band_list')


class DeleteBandView(View):

    def get_object(self, pk):
        return Band.objects.get(pk=pk)

    def get(self, request, pk):
        band = self.get_object(pk)
        return render(request, 'delete.html', {'band':band})

    def post(self, request, pk):
        band = self.get_object(pk)
        action = request.POST.get('action')
        if action == 'yes':
            band.delete()
        return redirect('band_list')

class ArticleListView(View):

    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'article_list.html', {'articles':articles})


class AddArticleView(View):

    def get(self, request):
        return render(request, 'article_add.html', {'status':Article.STATUS})

    def post(self, request):
        title = request.POST.get('title')
        author = request.POST.get('author')
        content = request.POST.get('content')
        emission_date = request.POST.get('emission_date')
        status = request.POST.get('status')
        Article.objects.create(title=title, author=author, content=content, status=status, start_emission=emission_date)
        return redirect('article_list')


class UpdateArticleView(View):

    def get_object(self, pk):
        return Article.objects.get(pk=pk)
    def get(self, request, pk):
        article = self.get_object(pk)
        return render(request, 'article_add.html', {'article':article, 'status':Article.STATUS})

    def post(self, request, pk):
        article = self.get_object(pk)
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.content = request.POST.get('content')
        article.status = request.POST.get('status')
        article.save()
        return redirect('article_list')


class DeleteArticleView(View):

    def get_object(self, pk):
        return Article.objects.get(pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        return render(request, 'delete.html', {'article':article})

    def post(self, request, pk):
        article = self.get_object(pk)
        action = request.POST.get('action')
        if action == 'yes':
            article.delete()
        return redirect('article_list')