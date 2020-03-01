from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from books.models import Book,Order
from cart.models import Cart
from books.forms import BookForm
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def show_books_view(request):
	context={}
	books_list = Book.objects.all()
	paginator = Paginator(books_list, 9) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context['books']=page_obj
	if request.user.is_authenticated:
		currentuser=request.user
		carti=Cart.objects.filter(user=currentuser)
		cartnumber=carti[0].books_in_cart()
		cartitems=carti[0].books.all()
		totalprice=carti[0].total_price()
		context['totalprice']=totalprice
		context['cart']=cartitems	
		context['cartnumber']=cartnumber
	return render(request,"books/bookslist.html",context)

def show_books_view_category(request,category):
	context={}	
	books_list = Book.objects.filter(category=category)
	paginator = Paginator(books_list, 9) 
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	context['books']=page_obj
	if request.user.is_authenticated:
		currentuser=request.user
		carti=Cart.objects.filter(user=currentuser)
		cartnumber=carti[0].books_in_cart()
		cartitems=carti[0].books.all()
		totalprice=carti[0].total_price()
		context['totalprice']=totalprice
		context['cart']=cartitems	
		context['cartnumber']=cartnumber
	return render(request,"books/booklistcategory.html",context)
@login_required(login_url='/login')
def add_book_view(request):
	if request.user.is_superuser:
		if request.method=="POST":
			book_form=BookForm(request.POST,request.FILES)
			if book_form.is_valid():
				book=book_form.save(commit=False)
				book.image=book_form.cleaned_data.get("image") 
				book.save()
				messages.success(request, 'Książka Dodana')
				book_form=BookForm()
				return render(request,'books/addbook.html',{
				'book_form': book_form,			
				})
		else:
			book_form=BookForm()
			return render(request,'books/addbook.html',{
			'book_form': book_form,			
			})
	else:
		return redirect('login')

	
@login_required(login_url='/login')
def show_oders_view(request):
	context={}
	currentuser=request.user
	orders=Order.objects.filter(user=currentuser)
	context['orders']=orders
	carti=Cart.objects.filter(user=currentuser)
	cartnumber=carti[0].books_in_cart()
	cartitems=carti[0].books.all()
	totalprice=carti[0].total_price()
	context['totalprice']=totalprice
	context['cart']=cartitems	
	context['cartnumber']=cartnumber
	return render(request,"books/orderlist.html",context)


def book_view(request,bookid):
	context={}
	book=Book.objects.filter(book_id=bookid).first()
	context['book']=book
	if request.user.is_authenticated:
		currentuser=request.user
		carti=Cart.objects.filter(user=currentuser)
		cartnumber=carti[0].books_in_cart()
		cartitems=carti[0].books.all()
		totalprice=carti[0].total_price()
		context['totalprice']=totalprice
		context['cart']=cartitems	
		context['cartnumber']=cartnumber
	return render(request,"books/book.html",context)

def search_book_view(request):
	context={}
	if request.method=="POST":
		query=request.POST.get('search')	
		books_list = Book.objects.search(query)
		paginator = Paginator(books_list, 9) 
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		context['books']=page_obj
	if request.user.is_authenticated:
		currentuser=request.user
		carti=Cart.objects.filter(user=currentuser)
		cartnumber=carti[0].books_in_cart()
		cartitems=carti[0].books.all()
		totalprice=carti[0].total_price()
		context['totalprice']=totalprice
		context['cart']=cartitems	
		context['cartnumber']=cartnumber
	return render(request,"books/search.html",context)	

