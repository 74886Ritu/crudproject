from django.shortcuts import render ,redirect
from BookApp.models import Book
def homePage(request):
    data =Book.objects.all()
    context ={}
    context['books'] = data
    return render(request,'home.html',context)


def addBook(request):
    if request.method =="GET" :
        return render (request,"add.html")
    else:
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        b=Book.objects.create(title=t,author=a,price=p)
        b.save()

        #print(t,a,p)
        #return render(request,'home.html')
# we need to excutee --> homepage(),but    
        return redirect('/home')
def deletebook(request,bookid):
    #print('delete book id:',bookid)
    b=Book.objects.filter(id=bookid)
    b.delete()
    return redirect('/home')


def updatebook(request,bookid):
    if request.method == "GET":
        print('update book id',bookid)
        b=Book.objects.filter(id=bookid)
        '''
         b is a 
        '''
        context ={}
        context['book'] = b[0]
        return render(request,'updatebook.html',context)
    else:

        #fetch the data
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        b= Book.objects.filter(id=bookid) # fetch the book object based on id
        b.update(title =t ,author=a ,price =p) #update will update will update all the book in the books in b with new t,a,p
        return redirect('/home')



        
    