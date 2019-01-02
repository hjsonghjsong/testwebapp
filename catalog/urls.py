from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('books/', views.BookListView.as_view(), name='books'),
 path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]
#urlpatterns = [
#    path('', views.index, name='index'),
#]
urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

urlpatterns += [
    path('returnBooks', views.list_allborrowedbooks.as_view(), name='return'),
]
