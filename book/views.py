from django.shortcuts import render,redirect
from .models import Book,Writer

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
    context={'writers':Writer.objects.all()}
    if request.method == "POST":
        
        name=request.POST['name']
        writer_name=request.POST['writer_name']
        if Book.objects.filter(name=name).exists():
            context['error']='This book is Taken'
            return render(request, 'book/addBook.html',context)
        else:
            
            Book.objects.create(name=name,writer_name=writer_name)
        

        return redirect("bookList")

    
    
    return render(request, 'book/addBook.html',context)

def updateBook(request,id):
    book=Book.objects.get(id=id)
    context={'writers':Writer.objects.all(),'book':book}

    if request.method == "POST":
            
            name=request.POST['name']
            writer_name=request.POST['writer_name']
            book.name=name
            book.writer_name=writer_name
            book.save()
            return redirect("bookList")

    return render(request, "book/updateBook.html",context)



def writerList(request):
    writers=Writer.objects.all()
    context={'writers':writers}
    return render(request, "writer/writerList.html",context)

def addWriter(request):
    if request.method == "POST":
        
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        if Writer.objects.filter(first_name=first_name,last_name=last_name).exists():
            
            return render(request, 'writer/addWriter.html',{'error':'This Writer is already haved'})
        else:
            
            Writer.objects.create(first_name=first_name,last_name=last_name)
        

        return redirect("writerList")
    return render(request, 'writer/addWriter.html')

def deleteWriter(request,id):
    writer=Writer.objects.get(id=id)
    writer.delete()
   
    
    return redirect("writerList")