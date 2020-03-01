from django.db import models
from account.models import User

from books.models import Book
# Create your models here.
class Cart(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")
	books=models.ManyToManyField(Book,blank=True)

	def total_price(self):
		books=self.books.all()
		price=0
		for book in books:
			price=price+book.price	
		return price

	def books_in_cart(self):
		booksnumber=self.books.all().count()
		return booksnumber
