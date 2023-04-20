from django.shortcuts import render,redirect
from .models import Book

# Create your views here.
from django.http import HttpResponse



def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def viewReturn(request):
    return render(request, "index.html")

def bookList(request):
    books=Book.objects.all()
    context={'books':books}

    return render(request, 'book/bookList.html',context)

def deleteBook(request,id):

    book=Book.objects.get(id=id)
    book.delete()
   
    
    return redirect("bookList")

def addNewBook(request):
    if request.method == "POST":
        
        name=request.POST['name']
        if Book.objects.filter(name=name).exists():
            
            return render(request, 'book/addBook.html',{'error':'This Book is Taken'})
        else:
            
            Book.objects.create(name=name)
        

        return redirect("bookList")

    return render(request, 'book/addBook.html')

def updateBook(request,id):
    book=Book.objects.get(id=id)
    if request.method == "POST":
            
            name=request.POST['name']
            book.name=name
            book.save()
            return redirect("bookList")


    
    
    
    return render(request, "book/updateBook.html",{'book':book})