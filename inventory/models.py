from django.db import models
from django.contrib.auth.models import User
class InventoryItem(models.Model):
	no = models.IntegerField()
	name = models.CharField(max_length=200)
	code = models.CharField(max_length=200,default="default")
	photo = models.ImageField(null=True, blank=True, upload_to='images/')
	quantity = models.IntegerField(default=0)
	department = models.CharField(max_length=200)
	category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
	location = models.CharField(max_length=255)
	pic = models.CharField(max_length=255)
	date_created = models.DateTimeField(auto_now_add=True)
	history = models.TextField()  # Added field
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name