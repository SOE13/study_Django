from django.shortcuts import render,redirect
from .models import Book,Writer,Users,FavBookCollection
from .form import UserFrom,WriterForm,BookForm,FavForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse



def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def loginPage(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request, user)
            return redirect('user')
    return render(request, "login.html")


def logoutPage(request):
    logout(request)
    return render(request, "login.html")

@login_required(login_url='login')
def user(request):
    context={'users':Users.objects.all()}
    context['form']=UserCreationForm()
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'user/user.html',{'users':Users.objects.all(),'form':form})
    return render(request, 'user/user.html',context)

@login_required(login_url='login')
def deleteUser(request,id):
    user=Users.objects.get(id=id)
    user.delete()
    return redirect("user")

@login_required(login_url='login')
def bookList(request):
    books=Book.objects.all()
    context={'books':books}

    return render(request, 'book/bookList.html',context)
    
@login_required(login_url='login')
def deleteBook(request,id):

    book=Book.objects.get(id=id)
    book.delete()
   
    
    return redirect("bookList")

@login_required(login_url='login')
def addNewBook(request):
    context={'writers':Writer.objects.all(),'form':BookForm()}
    if request.method == "POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()    
        return redirect("bookList")

    
    
    return render(request, 'book/addBook.html',context)

@login_required(login_url='login')
def updateBook(request,id):
    book=Book.objects.get(id=id)

    context={'writers':Writer.objects.all(),'form':BookForm(instance=book)}

    if request.method == "POST":
            
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()  
            return redirect("bookList")

    return render(request, "book/updateBook.html",context)


@login_required(login_url='login')
def writerList(request):
    writers=Writer.objects.all()
    context={'writers':writers}
    return render(request, "writer/writerList.html",context)

@login_required(login_url='login')
def addWriter(request):
    context={'form':WriterForm()}
    if request.method == "POST":
        form=WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("writerList")
        else:
            return render(request, 'writer/addWriter.html',{'form':form})
    return render(request, 'writer/addWriter.html',context)

@login_required(login_url='login')
def deleteWriter(request,id):
    
    writer=Writer.objects.get(id=id)
    writer.delete()
   
    
    return redirect("writerList")

@login_required(login_url='login')
def add_fav_book_collection(request):
    context={'favlist':FavBookCollection.objects.all()}
    context['form']=FavForm()
    if request.method == "POST":
        form=FavForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book/fav.html',context)