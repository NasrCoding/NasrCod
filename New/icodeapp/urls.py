from django.urls import path

from icodeapp.models import Category
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_result, name="search_results"),
    path('post/<slug:slug>/', views.post_detail, name='post_detail_url' ),
    path('category/<slug:slug>/', views.category_detail, name='category_detail_url'),
    path('register/', views.register, name="register"),
    path('post/<slug:slug>/leave-comment', views.leave_comment, name='leave_comment')



]

