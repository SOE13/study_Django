from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.home),
    path("",views.viewReturn),

    path('writerList/',views.writerList,name='writerList'),
    path('addWriter/',views.addWriter,name="addWriter"),
    path('deleteWriter/<int:id>/',views.deleteWriter,name="deleteWriter"),

    path("bookList/",views.bookList,name='bookList'),
    path('deleteBook/<int:id>/',views.deleteBook,name='deleteBook'),
    path('addBook/',views.addNewBook,name="addBook"),
    path('updateBook/<int:id>/',views.updateBook,name="updateBook")
]