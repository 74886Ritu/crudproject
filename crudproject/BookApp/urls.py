from django.urls import path
from BookApp import views
urlpatterns = [
    path('home',views.homePage),
    path('addbook',views.addBook),
    path('delete/<bookid>',views.deletebook),
    path('update/<bookid>',views.updatebook)
    
]