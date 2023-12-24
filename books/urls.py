from django.urls import path

from .views import BookListView, BookDetailsView, BookCreateView, BookUpdateView, BoolDeleteView
urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailsView.as_view(), name='book_detail'),
    path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BoolDeleteView.as_view(), name='book_delete'),


]
