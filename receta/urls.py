from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecetaList.as_view(), name='list'),
    path('create', views.RecetaCreate.as_view(), name='create'),
    path('<int:pk>/', views.RecetaDetail.as_view(), name='detail'),
    path('user/<int:pk>/', views.recipeByUser, name='find'),

]