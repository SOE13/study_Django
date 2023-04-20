from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home),
    path("",views.viewReturn),
    path("bookList/",views.bookList,name='bookList'),
    path('deleteBook/<int:id>/',views.deleteBook,name='deleteBook'),
    path('addBook/',views.addNewBook,name="addBook"),
    path('updateBook/<int:id>/',views.updateBook,name="updateBook")
]