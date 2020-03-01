from django.shortcuts import render,redirect,get_object_or_404
from account.models import User
from books.models import Book,Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.urls import resolve
from decimal import Decimal
from cart.models import Cart
# Create your views here.
@login_required(login_url='/login')
def add_to_cart(request,bookid):
	previous_url = request.META.get('HTTP_REFERER')
	user_cart=get_object_or_404(Cart,user=request.user)
	book=Book.objects.filter(book_id=bookid).first()
	if book in user_cart.books.all():
		user_cart.books.remove(book)
		user_cart.save()
	else:
		user_cart.books.add(book)
		user_cart.save()
	return redirect(previous_url)
@login_required(login_url='/login')
def add_oder_view(request):
	user_cart=get_object_or_404(Cart,user=request.user)
	user=request.user		
	if user_cart.books.all():
		if user.customer.have_enough(user_cart.total_price()):
			order=Order(user=user)
			order.save()
			for book in user_cart.books.all():			
				order.books.add(book)
			order.save()
			user.customer.money=user.customer.deducted_money(user_cart.total_price())
			user.customer.save()
			user_cart.books.clear()
			messages.success(request, 'Zamowienie Dodane')
		else:
			messages.error(request, 'Uzytkownik nie ma tyle pieniedzy')
			return redirect('summary')
	else:
		messages.error(request, 'Koszyk jest pusty')
		return redirect('summary')
	return redirect('home')

@login_required(login_url='/login')
def cart_summary_view(request):
	context={}
	user_cart=get_object_or_404(Cart,user=request.user)
	totalprice=user_cart.total_price()
	context['totalprice']=totalprice
	cartitems=user_cart.books.all()
	context['cart']=cartitems	
	return render(request,"cart/summarycart.html",context)