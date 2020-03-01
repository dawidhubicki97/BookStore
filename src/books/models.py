from django.db import models
from account.models import User
from django.db.models import Q
from django_resized import ResizedImageField
# Create your models here.

class BookManager(models.Manager):
	def search(self, query=None):
		qs = self.get_queryset()
		if query is not None:
			or_lookup = (Q(title__icontains=query) | 
						Q(description__icontains=query)|
						Q(writer__icontains=query)
						)
			qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
		return qs


class Book(models.Model):
	book_id=models.AutoField(primary_key=True)
	title=models.CharField(max_length=30)
	writer=models.CharField(max_length=30)
	category=models.CharField(max_length=30)
	price=models.DecimalField(max_digits=8, decimal_places=2,default=1)
	page_number=models.IntegerField()
	image=ResizedImageField(size=[352, 500],upload_to='book_image',null=True, blank=True)
	shortdescription = models.TextField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	objects=BookManager()








class Order(models.Model):
	order_id=models.AutoField(primary_key=True)
	books=models.ManyToManyField(Book)
	user=models.ForeignKey(User,on_delete=models.CASCADE)

	def total_price(self):
		books=self.books.all()
		price=0
		for book in books:
			price=price+book.price	
		return price