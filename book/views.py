from django.shortcuts import render,redirect
from .models import Book,Writer,Users,FavBookCollection
from .form import UserFrom,WriterForm,BookForm,FavForm

# Create your views here.
from django.http import HttpResponse



def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def login(request):
    if request.method == "POST":
        name=request.POST['name']
        password=request.POST['password']
        if Users.objects.filter(user_name=name).exists():
            user=Users.objects.get(user_name=name)
            if user.password==password:
                request.session['user']=name
                return redirect("user")
            else:
                return render(request, "login.html",{'password_error':"Wrong Password!"})
        else:
            return render(request, "login.html",{'user_error':"User Not found!"})
    return render(request, "login.html")


def logout(request):
    try:
        del request.session['user']
    except:
        pass
    return render(request, "login.html")

def user(request):
    try:
        user_name=request.session['user']
    except:
        return render(request, "login.html",{'login_error':'Login First'})

    context={'users':Users.objects.all()}
    context['form']=UserFrom()
    if request.method == "POST":
        form=UserFrom(request.POST)
        name=form['user_name'].value()
        password=form['password'].value()
        if Users.objects.filter(user_name=name).exists():
            context['error']='This User is Already exited'
        else:
            Users.objects.create(user_name=name,password=password)
    return render(request, 'user/user.html',context)

def deleteUser(request,id):
    user=Users.objects.get(id=id)
    user.delete()
    return redirect("user")

def bookList(request):
    books=Book.objects.all()
    context={'books':books}

    return render(request, 'book/bookList.html',context)

def deleteBook(request,id):

    book=Book.objects.get(id=id)
    book.delete()
   
    
    return redirect("bookList")

def addNewBook(request):
    context={'writers':Writer.objects.all(),'form':BookForm()}
    if request.method == "POST":
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()    

        return redirect("bookList")

    
    
    return render(request, 'book/addBook.html',context)

def updateBook(request,id):
    book=Book.objects.get(id=id)

    context={'writers':Writer.objects.all(),'form':BookForm(instance=book)}

    if request.method == "POST":
            
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()  
            return redirect("bookList")

    return render(request, "book/updateBook.html",context)



def writerList(request):
    writers=Writer.objects.all()
    context={'writers':writers}
    return render(request, "writer/writerList.html",context)

def addWriter(request):
    context={'form':WriterForm()}
    if request.method == "POST":
        form=WriterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("writerList")
        else:
            context['error']='This Writer already have'
    return render(request, 'writer/addWriter.html',context)

def deleteWriter(request,id):
    
    writer=Writer.objects.get(id=id)
    writer.delete()
   
    
    return redirect("writerList")

def add_fav_book_collection(request):
    context={'favlist':FavBookCollection.objects.all()}
    context['form']=FavForm()
    if request.method == "POST":
        form=FavForm(request.POST)
        form.save()
    return render(request, 'book/fav.html',context)