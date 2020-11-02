from django.db import models

class Address(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=100)
	phone = models.IntegerField()
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=40)
	gender = models.CharField(max_length=5)
	state = models.CharField(max_length=40)
	zipcode = models.CharField(max_length=10)

	def __str__(self):
		return self.name
