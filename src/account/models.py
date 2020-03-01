from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from decimal import Decimal
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class User(AbstractUser):
	is_customer=models.BooleanField(default=False)

	def __str__(self):
		return self.username

class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="customer")
	address= models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	phonenumber=PhoneNumberField(unique=True)
	money=models.DecimalField(max_digits=8, decimal_places=2,default=200)


	def have_enough(self,stake):
		if isinstance(stake,Decimal) or isinstance(stake,float) or isinstance(stake,int):
			if self.money>=stake:
				return True
			else:
				return False
		else:
			return False	

	def deducted_money(self,stake):
		if isinstance(stake,Decimal) or isinstance(stake,float) or isinstance(stake,int):
			return self.money-stake
		else:
			return self.money		



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	print('****', created)
	if instance.is_customer:
		Customer.objects.get_or_create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	print('_-----')	
	if instance.is_customer:
		instance.customer.save()	