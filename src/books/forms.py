from books.models import Book
from django.forms import ModelForm
from django import forms



class BookForm(forms.ModelForm):
	CHOICES = (
		(11,'Fantasy'),
		(12,'Literatura Historyczna'),
		(13,'Biografie'),
		(14,'Horror'),
		(15,'Romans'),
		(16,'Dramat'),
		(17,'Poezja'),
	)
	category = forms.ChoiceField(choices=CHOICES,label="Kategoria")
	class Meta:
		model=Book
		fields=('title','writer','price','category','page_number','image','shortdescription','description')
		labels = {
			'title': 'Tytuł',
			'writer': 'Pisarz',
			'price': 'Cena',
			'category': 'Kategoria',
			'page_number': 'Liczba Stron',
			'image': 'Obrazek',
			'shortdescription': 'Krótki opis',
			'description': 'Długi Opis',

		}