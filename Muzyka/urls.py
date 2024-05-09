"""
URL configuration for Muzyka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from moja_muzyka import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('bands/', views.BandListView.as_view(), name='band_list'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('add_band/', views.AddBandView.as_view(), name='band_add'),
    path('add_article/', views.AddArticleView.as_view(), name='article_add'),
    path('update_band/<int:pk>/', views.UpdateBandView.as_view(), name='band_update'),
    path('update_article/<int:pk>/', views.UpdateArticleView.as_view(), name='article_update'),
    path('delete_band/<int:pk>/', views.DeleteBandView.as_view(), name='band_delete'),
    path('delete_article/<int:pk>/', views.DeleteArticleView.as_view(), name='article_delete'),
]
