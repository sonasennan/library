from django.shortcuts import render
from books.models import Book
from books.forms import BookForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required
def addbooks(request):   #User defined
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,image=i)
        b.save()
        return viewbooks(request)
    return render(request,'addbooks.html')

@login_required
def viewb(request,p):
    b=Book.objects.get(id=p)
    return render(request,'viewb.html',{'b':b})

@login_required
def deletebook(request,p):
    b=Book.objects.get(id=p)
    b.delete()
    return viewbooks(request)

#built-in

# def addbooks(request):
#     if(request.method=="POST"):
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return viewbooks(request)
#
#     form=BookForm()      #empty form object
#     return render(request,"addbooks1.html",{'form':form})

@login_required
def viewbooks(request):
    b=Book.objects.all()
    return render(request,'viewbooks.html',{'book':b})

@login_required
def factorial(request):
    if(request.method=="POST"):
        n=int(request.POST['n'])
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return render(request,'fact.html',{'f':fact})

    return render(request,'fact.html')



@login_required
def editbook(request,p):
    b=Book.objects.get(id=p)
    if(request.method=="POST"):
        form=BookForm(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return viewbooks(request)


    form=BookForm(instance=b)
    return render(request,'editbook.html',{'f':form})