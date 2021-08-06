from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentListView.as_view(), name='list_docs'),
    path('<int:pk>/', views.DocumentView.as_view(), name='view_doc'),
    path('create/', views.DocumentCreateView.as_view(), name='create_doc'),
    path('<int:pk>/update/', views.DocumentUpdateView.as_view(), name='update_doc'),
]
