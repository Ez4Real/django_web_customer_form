import re
from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('', views.index, name='index'),
    path('forms/', views.FormListView.as_view(), name='forms'),
    path('form/<int:pk>/details', views.FormDetailView.as_view(), name='form-detail'),
    path('form/<int:pk>/update', views.edit_form, name='edit-form'),
    path('form/<int:pk>/printing', views.printing_form, name='form-print'),   
    path('form/create/', views.FormCreate.as_view(), name='form-create'),
    path('form/<int:pk>/delete/', views.FormDelete.as_view(), name='form-delete'),

]
